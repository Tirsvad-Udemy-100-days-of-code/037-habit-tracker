"""@file dry_run_pixela_gateway.py
@brief A Pixela gateway that prints the request and sends nothing.
"""

import json
from collections.abc import Mapping
from typing import TextIO

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.constants import (
    FIELD_TOKEN,
    HIDDEN_TOKEN,
    PIXELA_BASE_URL,
    TOKEN_HEADER,
)
from habit_tracker.infrastructure.http.urls import join_url

## @brief The names whose values are secrets and are hidden when printed.
_SECRET_NAMES = {FIELD_TOKEN, TOKEN_HEADER}


def _hide_secrets(values: Mapping[str, str]) -> dict[str, str]:
    """@brief Replace the secret values by the mask.

    @param values Header or body values.
    @return A copy in which the secrets are hidden.
    """
    return {k: HIDDEN_TOKEN if k in _SECRET_NAMES else v for k, v in values.items()}


class DryRunPixelaGateway:
    """@brief Shows what would be sent. Nothing leaves the computer."""

    def __init__(self, out: TextIO, base_url: str = PIXELA_BASE_URL) -> None:
        """@brief Create the gateway.

        @param out The stream the request is printed to.
        @param base_url The base URL of the API.
        """
        self._out = out
        self._base_url = base_url

    def post(
        self, path: str, body: Mapping[str, str], headers: Mapping[str, str]
    ) -> ApiResponse:
        """@brief Print the request with the token hidden.

        @param path The path below the base URL.
        @param body The JSON body.
        @param headers The extra HTTP headers.
        @return A successful response that says nothing was sent.
        """
        self._out.write(f"POST {join_url(self._base_url, path)}\n")
        for name, value in _hide_secrets(headers).items():
            self._out.write(f"{name}: {value}\n")
        self._out.write(json.dumps(_hide_secrets(body), indent=2) + "\n")
        return ApiResponse(200, "Dry run: nothing was sent.", True)
