"""@file test_create_user.py
@brief Unit tests of the create user use case, with a fake gateway.
"""

from collections.abc import Mapping
from dataclasses import dataclass, field

import pytest

from habit_tracker import create_user
from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.domain.value_objects.credentials import Credentials

CREDENTIALS = Credentials.of("jens-test", "abcdefgh12345")
SUCCESS = ApiResponse(200, "Success.", True)


@dataclass
class FakeGateway:
    """@brief A gateway that records the request and returns a set answer."""

    ## @brief The answer returned for every request.
    response: ApiResponse = SUCCESS

    ## @brief The recorded calls as (path, body, headers).
    calls: list[tuple[str, dict[str, str], dict[str, str]]] = field(
        default_factory=list
    )

    def post(
        self, path: str, body: Mapping[str, str], headers: Mapping[str, str]
    ) -> ApiResponse:
        """@brief Record the request and return the set answer."""
        self.calls.append((path, dict(body), dict(headers)))
        return self.response


def test_create_user_posts_to_the_users_path() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS)
    assert gateway.calls[0][0] == "users"


def test_create_user_sends_token_and_username() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS)
    body = gateway.calls[0][1]
    assert (body["token"], body["username"]) == ("abcdefgh12345", "jens-test")


def test_create_user_sends_yes_when_both_consents_are_given() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS, agree_terms=True, not_minor=True)
    body = gateway.calls[0][1]
    assert (body["agreeTermsOfService"], body["notMinor"]) == ("yes", "yes")


def test_create_user_sends_no_when_consents_are_declined() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS, agree_terms=False, not_minor=False)
    body = gateway.calls[0][1]
    assert (body["agreeTermsOfService"], body["notMinor"]) == ("no", "no")


def test_create_user_sends_exactly_the_four_fields() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS)
    assert set(gateway.calls[0][1]) == {
        "token",
        "username",
        "agreeTermsOfService",
        "notMinor",
    }


def test_create_user_sends_one_request() -> None:
    gateway = FakeGateway()
    create_user(gateway, CREDENTIALS)
    assert len(gateway.calls) == 1


def test_create_user_returns_the_response_on_success() -> None:
    assert create_user(FakeGateway(SUCCESS), CREDENTIALS) == SUCCESS


def test_create_user_returns_a_failed_result_when_status_is_409() -> None:
    taken = ApiResponse(409, "This username is already taken.", False)
    response = create_user(FakeGateway(taken), CREDENTIALS)
    assert response == taken


@pytest.mark.parametrize(
    ("username", "token"), [("Bad Name", "abcdefgh12345"), ("jens-test", "short")]
)
def test_invalid_input_is_rejected_before_any_gateway_call(
    username: str, token: str
) -> None:
    gateway = FakeGateway()
    with pytest.raises(InvalidInputError):
        create_user(gateway, Credentials.of(username, token))
    assert gateway.calls == []
