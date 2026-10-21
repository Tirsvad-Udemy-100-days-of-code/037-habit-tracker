"""@file test_pixel_domain.py
@brief Unit tests of the pixel value objects.
"""

import dataclasses
from datetime import date

import pytest

from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.domain.value_objects.pixel import Pixel
from habit_tracker.domain.value_objects.pixel_date import PixelDate
from habit_tracker.domain.value_objects.quantity import Quantity


def test_pixel_date_formats_a_date_as_year_month_day_without_separator() -> None:
    assert PixelDate(date(2026, 10, 22)).text == "20261022"


def test_pixel_date_str_is_the_compact_text() -> None:
    assert str(PixelDate(date(2026, 1, 2))) == "20260102"


@pytest.mark.parametrize("text", ["2026-10-22", "20261022", " 2026-10-22 "])
def test_pixel_date_parses_both_user_forms(text: str) -> None:
    assert PixelDate.parse(text) == PixelDate(date(2026, 10, 22))


@pytest.mark.parametrize(
    "text", ["2026-13-40", "abc", "", "2026-02-30", "2026-1-2", "2026102", "20261340"]
)
def test_pixel_date_is_rejected_when_it_is_not_a_real_date(text: str) -> None:
    with pytest.raises(InvalidInputError):
        PixelDate.parse(text)


@pytest.mark.parametrize("text", ["9.74", "5", "-3", "+2.5", ".5", "7."])
def test_quantity_keeps_the_number_text(text: str) -> None:
    assert Quantity(text).value == text


def test_quantity_removes_surrounding_white_space() -> None:
    assert str(Quantity(" 9.74 ")) == "9.74"


@pytest.mark.parametrize("text", ["", " ", "abc", "nan", "inf", "-inf", "1e5", "1,5"])
def test_quantity_is_rejected_when_it_is_not_a_finite_number(text: str) -> None:
    with pytest.raises(InvalidInputError):
        Quantity(text)


def test_pixel_is_immutable() -> None:
    pixel = Pixel(PixelDate(date(2026, 10, 22)), Quantity("1"))
    with pytest.raises(dataclasses.FrozenInstanceError):
        pixel.quantity = Quantity("2")  # type: ignore[misc]  # frozen on purpose
