"""@file post_pixel_command.py
@brief The `post-pixel` command.
"""

from argparse import ArgumentParser, Namespace

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.application.use_cases.post_pixel import post_pixel
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.pixel import Pixel
from habit_tracker.domain.value_objects.pixel_date import PixelDate
from habit_tracker.domain.value_objects.quantity import Quantity


class PostPixelCommand:
    """@brief Posts a pixel to a graph of the user named by the environment."""

    name = "post-pixel"
    help = "Post a pixel to a graph of the user of PIXELA_USERNAME"

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the pixel options.

        @param parser The parser of the command.
        """
        parser.add_argument("--graph-id", required=True, help="id of the graph")
        parser.add_argument(
            "--date", required=True, help="day, as YYYY-MM-DD or YYYYMMDD"
        )
        parser.add_argument(
            "--quantity", required=True, help="quantity, for example 9.74"
        )

    def execute(
        self, args: Namespace, gateway: PixelaGateway, credentials: Credentials
    ) -> ApiResponse:
        """@brief Run the post pixel use case.

        @param args The parsed arguments.
        @param gateway The port to Pixela.
        @param credentials The owner of the graph.
        @return The answer of Pixela.
        @throws InvalidInputError The graph id, date or quantity breaks a rule;
        nothing is sent.
        """
        pixel = Pixel(PixelDate.parse(args.date), Quantity(args.quantity))
        return post_pixel(gateway, credentials, GraphId(args.graph_id), pixel)
