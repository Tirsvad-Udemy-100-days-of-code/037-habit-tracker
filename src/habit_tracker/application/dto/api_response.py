"""@file api_response.py
@brief The answer of the Pixela API as plain data.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ApiResponse:
    """@brief What Pixela answered to one request."""

    ## @brief The HTTP status code.
    status_code: int

    ## @brief The message of Pixela, or a short text when it sent none.
    message: str

    ## @brief True when Pixela accepted the request.
    is_success: bool
