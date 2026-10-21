"""@file environment_credentials.py
@brief Read the Pixela credentials from the process environment.

The project never reads a `.env` file; the variables must be set in the
environment of the shell that starts the program.
"""

from collections.abc import Mapping

from habit_tracker.constants import ENV_TOKEN, ENV_USERNAME
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.infrastructure.config.configuration_error import ConfigurationError


def load_credentials(environ: Mapping[str, str]) -> Credentials:
    """@brief Build the credentials from the environment.

    @param environ The environment variables.
    @return The credentials.
    @throws ConfigurationError A variable is not set.
    @throws InvalidInputError A value breaks a Pixela rule.
    """
    username = environ.get(ENV_USERNAME)
    token = environ.get(ENV_TOKEN)
    if not username:
        raise ConfigurationError(f"The environment variable {ENV_USERNAME} is not set.")
    if not token:
        raise ConfigurationError(f"The environment variable {ENV_TOKEN} is not set.")
    return Credentials.of(username, token)
