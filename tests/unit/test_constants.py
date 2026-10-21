"""@file test_constants.py
@brief Unit tests of the constants module.
"""

from datetime import date

from habit_tracker import constants


def test_base_url_is_pixela_version_one() -> None:
    assert constants.PIXELA_BASE_URL == "https://pixe.la/v1"


def test_token_header_is_the_pixela_header() -> None:
    assert constants.TOKEN_HEADER == "X-USER-TOKEN"


def test_date_format_gives_year_month_day_without_separator() -> None:
    assert date(2026, 10, 22).strftime(constants.DATE_FORMAT) == "20261022"


def test_yes_and_no_are_the_pixela_values() -> None:
    assert (constants.VALUE_YES, constants.VALUE_NO) == ("yes", "no")
