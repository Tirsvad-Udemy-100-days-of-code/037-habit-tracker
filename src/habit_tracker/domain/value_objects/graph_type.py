"""@file graph_type.py
@brief The data type of the quantities of a Pixela graph.
"""

from enum import Enum


class GraphType(Enum):
    """@brief The quantity type of a graph, as Pixela names it."""

    ## @brief Whole numbers.
    INT = "int"

    ## @brief Decimal numbers.
    FLOAT = "float"
