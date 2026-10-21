"""@file endpoints.py
@brief The paths of the Pixela API below its base URL.
"""

from habit_tracker.constants import USERS_PATH


def users_path() -> str:
    """@brief Return the path of the users resource.

    @return The path used to create a user.
    """
    return USERS_PATH
