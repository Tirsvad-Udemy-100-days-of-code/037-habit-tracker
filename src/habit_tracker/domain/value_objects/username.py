"""@file username.py
@brief The Pixela username.
"""

import re
from dataclasses import dataclass

from habit_tracker.constants import USERNAME_PATTERN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class Username:
    """@brief A valid Pixela username.

    A username starts with a lower case letter and has 2 to 33 characters:
    lower case letters, digits and hyphens.
    """

    ## @brief The username text.
    value: str

    def __post_init__(self) -> None:
        """@brief Check the rule.

        @throws InvalidInputError The text does not match the username rule.
        """
        if re.fullmatch(USERNAME_PATTERN, self.value) is None:
            raise InvalidInputError(
                "The username must start with a lower case letter and have "
                "2 to 33 lower case letters, digits or hyphens."
            )

    def __str__(self) -> str:
        """@brief Return the username text."""
        return self.value
