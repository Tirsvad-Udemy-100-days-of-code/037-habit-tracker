"""@file create_graph.py
@brief Use case: create a Pixela graph (second step of the assignment).
"""

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.endpoints import graphs_path
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.constants import (
    FIELD_GRAPH_COLOR,
    FIELD_GRAPH_ID,
    FIELD_GRAPH_NAME,
    FIELD_GRAPH_TYPE,
    FIELD_GRAPH_UNIT,
    TOKEN_HEADER,
)
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph import Graph


def create_graph(
    gateway: PixelaGateway, credentials: Credentials, graph: Graph
) -> ApiResponse:
    """@brief Create a graph with a POST request.

    The token travels only in the `X-USER-TOKEN` header, never in the path or
    the body.

    @param gateway The port that sends the request.
    @param credentials The user that owns the graph.
    @param graph The graph to create.
    @return The answer of Pixela. A refusal is a response that is not a
    success, not an exception.
    @throws GatewayError The request could not be sent.
    """
    body = {
        FIELD_GRAPH_ID: str(graph.graph_id),
        FIELD_GRAPH_NAME: graph.name,
        FIELD_GRAPH_UNIT: graph.unit,
        FIELD_GRAPH_TYPE: graph.graph_type.value,
        FIELD_GRAPH_COLOR: graph.color.value,
    }
    headers = {TOKEN_HEADER: credentials.token.value}
    return gateway.post(graphs_path(credentials.username), body, headers)
