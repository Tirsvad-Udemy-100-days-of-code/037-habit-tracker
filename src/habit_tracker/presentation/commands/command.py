"""@file command.py
@brief The contract of a command line command.
"""

from argparse import ArgumentParser, Namespace
from typing import Protocol

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.domain.value_objects.credentials import Credentials


class Command(Protocol):
    """@brief One command of the program; it calls one use case."""

    ## @brief The name typed on the command line.
    name: str

    ## @brief The one line help text.
    help: str

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the arguments of the command.

        @param parser The parser of the command.
        """
        ...

    def execute(
        self, args: Namespace, gateway: PixelaGateway, credentials: Credentials
    ) -> ApiResponse:
        """@brief Run the use case.

        @param args The parsed arguments.
        @param gateway The port to Pixela.
        @param credentials The user of the request.
        @return The answer of Pixela.
        """
        ...
