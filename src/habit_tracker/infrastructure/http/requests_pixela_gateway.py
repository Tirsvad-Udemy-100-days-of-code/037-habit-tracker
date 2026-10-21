"""@file requests_pixela_gateway.py
@brief The Pixela gateway that sends real requests with the requests module.
"""

from collections.abc import Mapping

import requests

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.errors.gateway_error import GatewayError
from habit_tracker.constants import PIXELA_BASE_URL, REQUEST_TIMEOUT_SECONDS
from habit_tracker.infrastructure.http.urls import join_url


class RequestsPixelaGateway:
    """@brief Sends POST requests to Pixela with `requests`."""

    def __init__(
        self,
        base_url: str = PIXELA_BASE_URL,
        session: requests.Session | None = None,
    ) -> None:
        """@brief Create the gateway.

        @param base_url The base URL of the API.
        @param session The session to use and to close yourself; when omitted
        every request uses a session that is closed afterwards.
        """
        self._base_url = base_url
        self._session = session

    def post(
        self, path: str, body: Mapping[str, str], headers: Mapping[str, str]
    ) -> ApiResponse:
        """@brief Send a POST request with a JSON body.

        @param path The path below the base URL.
        @param body The JSON body.
        @param headers The extra HTTP headers.
        @return The answer of Pixela; a 4xx or 5xx answer is a response, not an
        exception.
        @throws GatewayError The request could not be sent.
        """
        url = join_url(self._base_url, path)
        try:
            if self._session is not None:
                response = self._send(self._session, url, body, headers)
            else:
                with requests.Session() as session:
                    response = self._send(session, url, body, headers)
        except requests.RequestException as error:
            raise GatewayError(
                f"Could not reach Pixela ({error.__class__.__name__})."
            ) from error
        return _to_api_response(response)

    @staticmethod
    def _send(
        session: requests.Session,
        url: str,
        body: Mapping[str, str],
        headers: Mapping[str, str],
    ) -> requests.Response:
        """@brief Send the request on a session.

        @param session The session.
        @param url The full URL.
        @param body The JSON body.
        @param headers The extra HTTP headers.
        @return The raw response.
        """
        return session.post(
            url,
            json=dict(body),
            headers=dict(headers),
            timeout=REQUEST_TIMEOUT_SECONDS,
        )


def _to_api_response(response: requests.Response) -> ApiResponse:
    """@brief Turn a `requests` response into an `ApiResponse`.

    @param response The response.
    @return The status code, the message and the success flag of Pixela.
    """
    status_code = int(response.status_code)
    try:
        payload = response.json()
    except ValueError:
        payload = None
    if isinstance(payload, dict):
        message = str(payload.get("message", ""))
        is_success = bool(payload.get("isSuccess", status_code < 400))
    else:
        message = ""
        is_success = status_code < 400
    return ApiResponse(status_code, message, is_success)
