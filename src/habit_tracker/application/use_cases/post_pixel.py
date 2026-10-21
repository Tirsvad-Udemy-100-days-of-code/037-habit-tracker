"""@file post_pixel.py
@brief Use case: post a pixel to a Pixela graph (third step of the assignment).
"""

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.endpoints import pixels_path
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.constants import (
    FIELD_PIXEL_DATE,
    FIELD_PIXEL_QUANTITY,
    TOKEN_HEADER,
)
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.pixel import Pixel


def post_pixel(
    gateway: PixelaGateway,
    credentials: Credentials,
    graph_id: GraphId,
    pixel: Pixel,
) -> ApiResponse:
    """@brief Post a pixel to a graph with a POST request.

    The date and the quantity are sent as strings. The token travels only in
    the `X-USER-TOKEN` header, never in the path or the body.

    @param gateway The port that sends the request.
    @param credentials The user that owns the graph.
    @param graph_id The graph that receives the pixel.
    @param pixel The date and quantity to record.
    @return The answer of Pixela. A refusal is a response that is not a
    success, not an exception.
    @throws GatewayError The request could not be sent.
    """
    body = {
        FIELD_PIXEL_DATE: pixel.date.text,
        FIELD_PIXEL_QUANTITY: str(pixel.quantity),
    }
    headers = {TOKEN_HEADER: credentials.token.value}
    path = pixels_path(credentials.username, graph_id)
    return gateway.post(path, body, headers)
