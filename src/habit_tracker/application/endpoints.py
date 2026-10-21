"""@file endpoints.py
@brief The paths of the Pixela API below its base URL.
"""

from habit_tracker.constants import GRAPHS_PATH, USERS_PATH
from habit_tracker.domain.value_objects.username import Username


def users_path() -> str:
    """@brief Return the path of the users resource.

    @return The path used to create a user.
    """
    return USERS_PATH


def graphs_path(username: Username) -> str:
    """@brief Return the path of the graphs resource of one user.

    @param username The owner of the graphs.
    @return The path used to create a graph.
    """
    return f"{USERS_PATH}/{username}/{GRAPHS_PATH}"
