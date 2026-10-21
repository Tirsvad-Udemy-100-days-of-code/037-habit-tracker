"""@file output.py
@brief How the program writes the answer of Pixela and the exit code.
"""

from typing import TextIO

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.constants import EXIT_OK, EXIT_REJECTED


def write_response(out: TextIO, response: ApiResponse) -> int:
    """@brief Write the answer and return the exit code.

    @param out The stream to write to.
    @param response The answer of Pixela.
    @return `EXIT_OK` for a success, `EXIT_REJECTED` otherwise.
    """
    outcome = "Success" if response.is_success else "Rejected"
    out.write(f"{outcome} ({response.status_code}): {response.message}\n")
    return EXIT_OK if response.is_success else EXIT_REJECTED
