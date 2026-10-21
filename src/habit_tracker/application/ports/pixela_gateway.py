"""@file pixela_gateway.py
@brief The port through which the use cases talk to the Pixela API.
"""

from collections.abc import Mapping
from typing import Protocol

from habit_tracker.application.dto.api_response import ApiResponse


class PixelaGateway(Protocol):
    """@brief Sends one JSON POST request to the Pixela API."""

    def post(
        self, path: str, body: Mapping[str, str], headers: Mapping[str, str]
    ) -> ApiResponse:
        """@brief Send a POST request.

        @param path The path below the API base URL, for example `users`.
        @param body The JSON body.
        @param headers The extra HTTP headers.
        @return The answer of Pixela.
        @throws GatewayError The request could not be sent.
        """
        ...
