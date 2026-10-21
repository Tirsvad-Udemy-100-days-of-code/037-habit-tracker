"""@file cli.py
@brief The command line: composition root of the program.

This is the one place that builds the adapters and hands them to the commands.
"""

import argparse
import os
import sys
from collections.abc import Mapping, Sequence
from typing import TextIO

from habit_tracker.application.errors.gateway_error import GatewayError
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.constants import (
    EXIT_INVALID,
    EXIT_UNREACHABLE,
    PIXELA_BASE_URL,
    PROGRAM_NAME,
)
from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.infrastructure.config.configuration_error import ConfigurationError
from habit_tracker.infrastructure.config.environment_credentials import (
    load_credentials,
)
from habit_tracker.infrastructure.http.dry_run_pixela_gateway import (
    DryRunPixelaGateway,
)
from habit_tracker.infrastructure.http.requests_pixela_gateway import (
    RequestsPixelaGateway,
)
from habit_tracker.presentation.commands.command import Command
from habit_tracker.presentation.commands.create_user_command import CreateUserCommand
from habit_tracker.presentation.shared.output import write_response

## @brief The commands of the program, one per use case.
COMMANDS: tuple[Command, ...] = (CreateUserCommand(),)


def build_parser(commands: Sequence[Command]) -> argparse.ArgumentParser:
    """@brief Build the argument parser.

    @param commands The commands to offer.
    @return The parser, with one sub command per command.
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME, description="Track a habit with the Pixela API."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the request with the token hidden and send nothing",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in commands:
        command.configure(subparsers.add_parser(command.name, help=command.help))
    return parser


def main(
    argv: Sequence[str] | None = None,
    environ: Mapping[str, str] | None = None,
    out: TextIO | None = None,
    base_url: str = PIXELA_BASE_URL,
) -> int:
    """@brief Run the program.

    @param argv The arguments; `sys.argv` when omitted.
    @param environ The environment; `os.environ` when omitted.
    @param out The output stream; standard output when omitted.
    @param base_url The base URL of the API.
    @return The exit code.
    """
    stream = out if out is not None else sys.stdout
    env = environ if environ is not None else os.environ
    args = build_parser(COMMANDS).parse_args(argv)
    command = next(c for c in COMMANDS if c.name == args.command)
    gateway: PixelaGateway
    if args.dry_run:
        gateway = DryRunPixelaGateway(stream, base_url)
    else:
        gateway = RequestsPixelaGateway(base_url)
    try:
        credentials = load_credentials(env)
        response = command.execute(args, gateway, credentials)
    except (InvalidInputError, ConfigurationError) as error:
        stream.write(f"Error: {error}\n")
        return EXIT_INVALID
    except GatewayError as error:
        stream.write(f"Error: {error}\n")
        return EXIT_UNREACHABLE
    return write_response(stream, response)
