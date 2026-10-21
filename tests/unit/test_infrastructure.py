"""@file test_infrastructure.py
@brief Unit tests of the infrastructure pieces that need no network.
"""

import json
from io import StringIO
from typing import Any, cast

import pytest
import requests

from habit_tracker.application.errors.gateway_error import GatewayError
from habit_tracker.constants import HIDDEN_TOKEN, REQUEST_TIMEOUT_SECONDS
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)
from habit_tracker.infrastructure.config.environment_credentials import (
    load_credentials,
)
from habit_tracker.infrastructure.http.dry_run_pixela_gateway import (
    DryRunPixelaGateway,
)
from habit_tracker.infrastructure.http.requests_pixela_gateway import (
    RequestsPixelaGateway,
)
from habit_tracker.infrastructure.http.urls import join_url

SECRET = "abcdefgh12345"
BODY = {"token": SECRET, "username": "jens-test"}


class FakeResponse:
    """@brief A hand-written stand-in for `requests.Response`."""

    def __init__(
        self, status_code: int, payload: object = None, is_json: bool = True
    ) -> None:
        """@brief Set the answer.

        @param status_code The HTTP status code.
        @param payload The decoded JSON body.
        @param is_json False when the body is not JSON.
        """
        self.status_code = status_code
        self._payload = payload
        self._is_json = is_json

    def json(self) -> object:
        """@brief Return the payload or fail like a non-JSON body."""
        if not self._is_json:
            raise ValueError("not json")
        return self._payload


class FakeSession:
    """@brief A hand-written stand-in for `requests.Session`."""

    def __init__(
        self, response: FakeResponse | None = None, error: Exception | None = None
    ) -> None:
        """@brief Set the answer or the error raised by `post`."""
        self.response = response if response is not None else FakeResponse(200, {})
        self.error = error
        self.calls: list[tuple[str, dict[str, Any]]] = []

    def post(self, url: str, **kwargs: Any) -> FakeResponse:
        """@brief Record the call and answer."""
        self.calls.append((url, kwargs))
        if self.error is not None:
            raise self.error
        return self.response


def _gateway(session: FakeSession) -> RequestsPixelaGateway:
    """@brief Build the gateway around the fake session."""
    return RequestsPixelaGateway(session=cast(requests.Session, session))


def test_join_url_uses_exactly_one_slash() -> None:
    assert join_url("https://pixe.la/v1/", "/users") == "https://pixe.la/v1/users"


def test_join_url_adds_a_slash_when_none_is_given() -> None:
    assert join_url("https://pixe.la/v1", "users") == "https://pixe.la/v1/users"


def test_dry_run_hides_the_token_in_the_body() -> None:
    out = StringIO()
    DryRunPixelaGateway(out).post("users", BODY, {})
    assert SECRET not in out.getvalue()
    assert HIDDEN_TOKEN in out.getvalue()


def test_dry_run_hides_the_token_in_the_header() -> None:
    out = StringIO()
    DryRunPixelaGateway(out).post("graphs", {}, {"X-USER-TOKEN": SECRET})
    assert SECRET not in out.getvalue()
    assert f"X-USER-TOKEN: {HIDDEN_TOKEN}" in out.getvalue()


def test_dry_run_prints_method_and_url() -> None:
    out = StringIO()
    DryRunPixelaGateway(out).post("users", BODY, {})
    assert out.getvalue().startswith("POST https://pixe.la/v1/users\n")


def test_dry_run_keeps_other_fields_visible() -> None:
    out = StringIO()
    DryRunPixelaGateway(out).post("users", BODY, {})
    assert '"username": "jens-test"' in out.getvalue()


def test_dry_run_returns_a_success() -> None:
    response = DryRunPixelaGateway(StringIO()).post("users", BODY, {})
    assert response.is_success is True


def test_dry_run_prints_a_valid_json_body() -> None:
    out = StringIO()
    DryRunPixelaGateway(out).post("users", BODY, {})
    printed = out.getvalue().split("\n", 1)[1]
    assert json.loads(printed)["token"] == HIDDEN_TOKEN


def test_load_credentials_builds_credentials_from_the_environment() -> None:
    environ = {"PIXELA_USERNAME": "jens-test", "PIXELA_TOKEN": SECRET}
    credentials = load_credentials(environ)
    assert (str(credentials.username), credentials.token.value) == (
        "jens-test",
        SECRET,
    )


def test_load_credentials_fails_when_username_is_missing() -> None:
    with pytest.raises(ConfigurationError, match="PIXELA_USERNAME"):
        load_credentials({"PIXELA_TOKEN": SECRET})


def test_load_credentials_fails_when_token_is_missing() -> None:
    with pytest.raises(ConfigurationError, match="PIXELA_TOKEN"):
        load_credentials({"PIXELA_USERNAME": "jens-test"})


def test_load_credentials_fails_when_username_is_empty() -> None:
    with pytest.raises(ConfigurationError):
        load_credentials({"PIXELA_USERNAME": "", "PIXELA_TOKEN": SECRET})


def test_load_credentials_rejects_an_invalid_username() -> None:
    with pytest.raises(InvalidInputError):
        load_credentials({"PIXELA_USERNAME": "Bad Name", "PIXELA_TOKEN": SECRET})


def test_load_credentials_rejects_an_invalid_token() -> None:
    with pytest.raises(InvalidInputError):
        load_credentials({"PIXELA_USERNAME": "jens-test", "PIXELA_TOKEN": "short"})


def test_requests_gateway_posts_to_the_pixela_users_url() -> None:
    session = FakeSession()
    _gateway(session).post("users", BODY, {})
    assert session.calls[0][0] == "https://pixe.la/v1/users"


def test_requests_gateway_sends_the_body_as_json() -> None:
    session = FakeSession()
    _gateway(session).post("users", BODY, {})
    assert session.calls[0][1]["json"] == BODY


def test_requests_gateway_sends_the_headers() -> None:
    session = FakeSession()
    _gateway(session).post("users", BODY, {"X-USER-TOKEN": SECRET})
    assert session.calls[0][1]["headers"] == {"X-USER-TOKEN": SECRET}


def test_requests_gateway_uses_the_timeout_of_the_constants() -> None:
    session = FakeSession()
    _gateway(session).post("users", BODY, {})
    assert session.calls[0][1]["timeout"] == REQUEST_TIMEOUT_SECONDS


def test_requests_gateway_reads_message_and_success_from_the_body() -> None:
    session = FakeSession(FakeResponse(409, {"message": "Taken.", "isSuccess": False}))
    response = _gateway(session).post("users", BODY, {})
    assert (response.status_code, response.message, response.is_success) == (
        409,
        "Taken.",
        False,
    )


def test_requests_gateway_returns_a_4xx_answer_without_raising() -> None:
    session = FakeSession(FakeResponse(404, {"message": "Nope."}))
    assert _gateway(session).post("users", BODY, {}).is_success is False


def test_requests_gateway_handles_a_body_that_is_not_json() -> None:
    session = FakeSession(FakeResponse(502, is_json=False))
    response = _gateway(session).post("users", BODY, {})
    assert (response.status_code, response.message, response.is_success) == (
        502,
        "",
        False,
    )


def test_requests_gateway_treats_a_non_json_2xx_answer_as_success() -> None:
    session = FakeSession(FakeResponse(200, is_json=False))
    assert _gateway(session).post("users", BODY, {}).is_success is True


def test_requests_gateway_handles_a_json_body_that_is_not_an_object() -> None:
    session = FakeSession(FakeResponse(200, ["unexpected"]))
    assert _gateway(session).post("users", BODY, {}).message == ""


def test_requests_gateway_raises_gateway_error_on_request_exception() -> None:
    session = FakeSession(error=requests.ConnectionError("boom"))
    with pytest.raises(GatewayError):
        _gateway(session).post("users", BODY, {})


def test_requests_gateway_keeps_the_cause_of_the_failure() -> None:
    cause = requests.Timeout("slow")
    session = FakeSession(error=cause)
    with pytest.raises(GatewayError) as info:
        _gateway(session).post("users", BODY, {})
    assert info.value.__cause__ is cause


def test_requests_gateway_error_message_hides_the_token() -> None:
    session = FakeSession(error=requests.ConnectionError(SECRET))
    with pytest.raises(GatewayError) as info:
        _gateway(session).post("users", BODY, {})
    assert SECRET not in str(info.value)


def test_requests_gateway_creates_its_own_session_when_none_is_given() -> None:
    gateway = RequestsPixelaGateway()
    assert isinstance(gateway, RequestsPixelaGateway)
