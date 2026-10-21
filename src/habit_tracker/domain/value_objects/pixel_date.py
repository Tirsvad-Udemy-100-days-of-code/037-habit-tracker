"""@file pixel_date.py
@brief The date of a pixel.
"""

import re
from dataclasses import dataclass
from datetime import date, datetime

from habit_tracker.constants import DATE_FORMAT, INPUT_DATE_FORMAT, INPUT_DATE_PATTERN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class PixelDate:
    """@brief A day of a pixel, sent to Pixela as `YYYYMMDD`."""

    ## @brief The calendar day.
    day: date

    @classmethod
    def parse(cls, text: str) -> "PixelDate":
        """@brief Build a pixel date from user text.

        @param text A date such as `2026-10-22` or `20261022`.
        @return The pixel date.
        @throws InvalidInputError The text is not a real date in either form.
        """
        cleaned = text.strip()
        if re.fullmatch(INPUT_DATE_PATTERN, cleaned) is None:
            raise InvalidInputError(
                "The date must be written as YYYY-MM-DD or YYYYMMDD."
            )
        date_format = INPUT_DATE_FORMAT if "-" in cleaned else DATE_FORMAT
        try:
            return cls(datetime.strptime(cleaned, date_format).date())
        except ValueError as error:
            raise InvalidInputError("The date does not exist.") from error

    @property
    def text(self) -> str:
        """@brief The date as `YYYYMMDD`, the format Pixela expects."""
        return self.day.strftime(DATE_FORMAT)

    def __str__(self) -> str:
        """@brief Return the date as `YYYYMMDD`."""
        return self.text
