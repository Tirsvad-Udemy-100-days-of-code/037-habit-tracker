"""@file create_graph_command.py
@brief The `create-graph` command.
"""

from argparse import ArgumentParser, Namespace

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.application.use_cases.create_graph import create_graph
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph import Graph
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType


class CreateGraphCommand:
    """@brief Creates a graph for the user named by the environment."""

    name = "create-graph"
    help = "Create a graph for the user of PIXELA_USERNAME"

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the graph options.

        @param parser The parser of the command.
        """
        parser.add_argument("--id", required=True, help="graph id, for example run1")
        parser.add_argument("--name", required=True, help="graph name")
        parser.add_argument("--unit", required=True, help="unit, for example km")
        parser.add_argument(
            "--type",
            choices=[t.value for t in GraphType],
            default=GraphType.FLOAT.value,
            help="quantity type (default: %(default)s)",
        )
        parser.add_argument(
            "--color",
            choices=[c.value for c in GraphColor],
            default=GraphColor.AJISAI.value,
            help="graph colour (default: %(default)s)",
        )

    def execute(
        self, args: Namespace, gateway: PixelaGateway, credentials: Credentials
    ) -> ApiResponse:
        """@brief Run the create graph use case.

        @param args The parsed arguments.
        @param gateway The port to Pixela.
        @param credentials The owner of the graph.
        @return The answer of Pixela.
        @throws InvalidInputError The graph breaks a rule; nothing is sent.
        """
        graph = Graph(
            GraphId(args.id),
            args.name,
            args.unit,
            GraphType(args.type),
            GraphColor(args.color),
        )
        return create_graph(gateway, credentials, graph)
