"""@file test_domain.py
@brief Unit tests of the domain value objects.
"""

import pytest

from habit_tracker.constants import HIDDEN_TOKEN
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.token import Token
from habit_tracker.domain.value_objects.username import Username

SECRET = "abcdefgh12345"


def test_username_is_accepted_when_it_follows_the_rule() -> None:
    assert Username("jens-test").value == "jens-test"


def test_username_str_is_the_text() -> None:
    assert str(Username("jens-test")) == "jens-test"


def test_username_is_accepted_at_the_shortest_length() -> None:
    assert Username("ab").value == "ab"


def test_username_is_accepted_at_the_longest_length() -> None:
    assert Username("a" * 33).value == "a" * 33


@pytest.mark.parametrize(
    "text",
    ["", "a", "a" * 34, "1abc", "-abc", "Jens", "jens_test", "jens test", "jens.t"],
)
def test_username_is_rejected_when_it_breaks_the_rule(text: str) -> None:
    with pytest.raises(InvalidInputError):
        Username(text)


def test_token_is_accepted_when_it_follows_the_rule() -> None:
    assert Token(SECRET).value == SECRET


def test_token_is_accepted_at_the_shortest_length() -> None:
    assert Token("a" * 8).value == "a" * 8


def test_token_is_accepted_at_the_longest_length() -> None:
    assert Token("a" * 128).value == "a" * 128


@pytest.mark.parametrize(
    "text", ["", "short12", "a" * 129, "has space1", "tab\tchar12", "accenté123"]
)
def test_token_is_rejected_when_it_breaks_the_rule(text: str) -> None:
    with pytest.raises(InvalidInputError):
        Token(text)


def test_token_str_hides_the_secret() -> None:
    assert str(Token(SECRET)) == HIDDEN_TOKEN


def test_token_repr_hides_the_secret() -> None:
    assert SECRET not in repr(Token(SECRET))


def test_token_error_message_hides_the_secret() -> None:
    with pytest.raises(InvalidInputError) as info:
        Token("bad token")
    assert "bad token" not in str(info.value)


def test_credentials_repr_hides_the_secret() -> None:
    assert SECRET not in repr(Credentials.of("jens-test", SECRET))


def test_credentials_of_builds_value_objects_from_text() -> None:
    credentials = Credentials.of("jens-test", SECRET)
    assert (credentials.username, credentials.token) == (
        Username("jens-test"),
        Token(SECRET),
    )


def test_credentials_of_rejects_an_invalid_username() -> None:
    with pytest.raises(InvalidInputError):
        Credentials.of("Bad Name", SECRET)


def test_credentials_of_rejects_an_invalid_token() -> None:
    with pytest.raises(InvalidInputError):
        Credentials.of("jens-test", "short")
