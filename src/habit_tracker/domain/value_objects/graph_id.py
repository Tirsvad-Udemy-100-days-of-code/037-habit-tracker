"""@file graph_id.py
@brief The Pixela graph identifier.
"""

import re
from dataclasses import dataclass

from habit_tracker.constants import GRAPH_ID_PATTERN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class GraphId:
    """@brief A valid Pixela graph id.

    A graph id starts with a lower case letter and has 2 to 17 characters:
    lower case letters, digits and hyphens.
    """

    ## @brief The graph id text.
    value: str

    def __post_init__(self) -> None:
        """@brief Check the rule.

        @throws InvalidInputError The text does not match the graph id rule.
        """
        if re.fullmatch(GRAPH_ID_PATTERN, self.value) is None:
            raise InvalidInputError(
                "The graph id must start with a lower case letter and have "
                "2 to 17 lower case letters, digits or hyphens."
            )

    def __str__(self) -> str:
        """@brief Return the graph id text."""
        return self.value
