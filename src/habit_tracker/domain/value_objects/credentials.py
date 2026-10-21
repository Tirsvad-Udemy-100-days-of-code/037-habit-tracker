"""@file credentials.py
@brief The username and token of one Pixela user.
"""

from dataclasses import dataclass

from habit_tracker.domain.value_objects.token import Token
from habit_tracker.domain.value_objects.username import Username


@dataclass(frozen=True, slots=True)
class Credentials:
    """@brief The username and the token that identify a Pixela user."""

    ## @brief The username.
    username: Username

    ## @brief The secret token.
    token: Token

    @classmethod
    def of(cls, username: str, token: str) -> "Credentials":
        """@brief Build credentials from plain text.

        @param username The username text.
        @param token The token text.
        @return The credentials.
        @throws InvalidInputError The username or the token breaks its rule.
        """
        return cls(Username(username), Token(token))
