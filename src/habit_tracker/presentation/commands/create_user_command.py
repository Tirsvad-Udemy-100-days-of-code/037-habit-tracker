"""@file create_user_command.py
@brief The `create-user` command.
"""

from argparse import ArgumentParser, Namespace

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.application.use_cases.create_user import create_user
from habit_tracker.domain.value_objects.credentials import Credentials


class CreateUserCommand:
    """@brief Creates the Pixela user named by the environment."""

    name = "create-user"
    help = "Create the Pixela user of PIXELA_USERNAME and PIXELA_TOKEN"

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the two consent flags.

        @param parser The parser of the command.
        """
        parser.add_argument(
            "--agree-terms",
            action="store_true",
            help="accept the Pixela terms of service",
        )
        parser.add_argument(
            "--not-minor", action="store_true", help="confirm that you are not a minor"
        )

    def execute(
        self, args: Namespace, gateway: PixelaGateway, credentials: Credentials
    ) -> ApiResponse:
        """@brief Run the create user use case.

        @param args The parsed arguments.
        @param gateway The port to Pixela.
        @param credentials The new user.
        @return The answer of Pixela.
        """
        return create_user(
            gateway,
            credentials,
            agree_terms=args.agree_terms,
            not_minor=args.not_minor,
        )
