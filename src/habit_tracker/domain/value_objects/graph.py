"""@file graph.py
@brief The definition of one Pixela graph.
"""

from dataclasses import dataclass

from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType


@dataclass(frozen=True, slots=True)
class Graph:
    """@brief A graph to create: id, name, unit, quantity type and colour."""

    ## @brief The graph id.
    graph_id: GraphId

    ## @brief The display name; not empty.
    name: str

    ## @brief The unit of measure, for example `km`; not empty.
    unit: str

    ## @brief The quantity type.
    graph_type: GraphType

    ## @brief The colour.
    color: GraphColor

    def __post_init__(self) -> None:
        """@brief Check the rules.

        @throws InvalidInputError The name or the unit is empty.
        """
        if not self.name.strip():
            raise InvalidInputError("The graph name must not be empty.")
        if not self.unit.strip():
            raise InvalidInputError("The graph unit must not be empty.")
