"""@file test_create_graph.py
@brief Unit tests of the create graph use case, with a fake gateway.
"""

from collections.abc import Mapping
from dataclasses import dataclass, field

from habit_tracker import create_graph
from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph import Graph
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType

SECRET = "abcdefgh12345"
CREDENTIALS = Credentials.of("jens-test", SECRET)
GRAPH = Graph(GraphId("run1"), "Running", "km", GraphType.FLOAT, GraphColor.AJISAI)
SUCCESS = ApiResponse(200, "Success.", True)


@dataclass
class FakeGateway:
    """@brief A gateway that records the request and returns a set answer."""

    ## @brief The answer returned for every request.
    response: ApiResponse = SUCCESS

    ## @brief The recorded calls as (path, body, headers).
    calls: list[tuple[str, dict[str, str], dict[str, str]]] = field(
        default_factory=list
    )

    def post(
        self, path: str, body: Mapping[str, str], headers: Mapping[str, str]
    ) -> ApiResponse:
        """@brief Record the request and return the set answer."""
        self.calls.append((path, dict(body), dict(headers)))
        return self.response


def test_create_graph_posts_to_the_graphs_path_of_the_user() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert gateway.calls[0][0] == "users/jens-test/graphs"


def test_create_graph_sends_the_five_graph_fields() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert gateway.calls[0][1] == {
        "id": "run1",
        "name": "Running",
        "unit": "km",
        "type": "float",
        "color": "ajisai",
    }


def test_create_graph_sends_the_token_in_the_header() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert gateway.calls[0][2] == {"X-USER-TOKEN": SECRET}


def test_create_graph_keeps_the_token_out_of_the_path() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert SECRET not in gateway.calls[0][0]


def test_create_graph_keeps_the_token_out_of_the_body() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert SECRET not in gateway.calls[0][1].values()
    assert "token" not in gateway.calls[0][1]


def test_create_graph_sends_one_request() -> None:
    gateway = FakeGateway()
    create_graph(gateway, CREDENTIALS, GRAPH)
    assert len(gateway.calls) == 1


def test_create_graph_returns_the_response_on_success() -> None:
    assert create_graph(FakeGateway(SUCCESS), CREDENTIALS, GRAPH) == SUCCESS


def test_create_graph_returns_a_failed_result_when_status_is_409() -> None:
    refused = ApiResponse(409, "This graphID already exists.", False)
    assert create_graph(FakeGateway(refused), CREDENTIALS, GRAPH) == refused
