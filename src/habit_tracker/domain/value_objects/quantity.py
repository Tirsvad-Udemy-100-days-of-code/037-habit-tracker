"""@file quantity.py
@brief The quantity of a pixel.
"""

import re
from dataclasses import dataclass

from habit_tracker.constants import QUANTITY_PATTERN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class Quantity:
    """@brief A finite number kept as text, for example `9.74`.

    Pixela expects the quantity as a string, so the text the user typed is
    kept; only surrounding white space is removed.
    """

    ## @brief The number as text.
    value: str

    def __post_init__(self) -> None:
        """@brief Normalise and check the rule.

        @throws InvalidInputError The text is not a finite decimal number.
        """
        cleaned = self.value.strip()
        if re.fullmatch(QUANTITY_PATTERN, cleaned) is None:
            raise InvalidInputError("The quantity must be a number such as 5 or 9.74.")
        object.__setattr__(self, "value", cleaned)

    def __str__(self) -> str:
        """@brief Return the quantity text."""
        return self.value
