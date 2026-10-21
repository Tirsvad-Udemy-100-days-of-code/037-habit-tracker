"""@file pixel.py
@brief One pixel of a graph.
"""

from dataclasses import dataclass

from habit_tracker.domain.value_objects.pixel_date import PixelDate
from habit_tracker.domain.value_objects.quantity import Quantity


@dataclass(frozen=True, slots=True)
class Pixel:
    """@brief The quantity achieved on one day."""

    ## @brief The day of the pixel.
    date: PixelDate

    ## @brief The quantity of the day.
    quantity: Quantity
