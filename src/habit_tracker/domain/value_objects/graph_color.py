"""@file graph_color.py
@brief The colours Pixela accepts for a graph.
"""

from enum import Enum


class GraphColor(Enum):
    """@brief The colour of a graph, as Pixela names it."""

    ## @brief Green.
    SHIBAFU = "shibafu"

    ## @brief Red.
    MOMIJI = "momiji"

    ## @brief Blue.
    SORA = "sora"

    ## @brief Yellow.
    ICHOU = "ichou"

    ## @brief Purple.
    AJISAI = "ajisai"

    ## @brief Black.
    KURO = "kuro"
