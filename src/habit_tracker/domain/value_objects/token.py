"""@file token.py
@brief The Pixela token, the secret that authenticates a user.
"""

import re
from dataclasses import dataclass, field

from habit_tracker.constants import HIDDEN_TOKEN, TOKEN_PATTERN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class Token:
    """@brief A valid Pixela token.

    A token has 8 to 128 printable ASCII characters and no space. It is a
    secret: its text is hidden in the representation and in `str`.
    """

    ## @brief The secret text. It is left out of `repr`.
    value: str = field(repr=False)

    def __post_init__(self) -> None:
        """@brief Check the rule.

        @throws InvalidInputError The text does not match the token rule. The
        message never contains the text.
        """
        if re.fullmatch(TOKEN_PATTERN, self.value) is None:
            raise InvalidInputError(
                "The token must have 8 to 128 printable ASCII characters and no space."
            )

    def __str__(self) -> str:
        """@brief Return the mask, never the secret."""
        return HIDDEN_TOKEN
