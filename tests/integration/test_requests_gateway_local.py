"""@file test_requests_gateway_local.py
@brief Integration tests of the real requests gateway against a local server.
"""

import pytest

from habit_tracker.application.errors.gateway_error import GatewayError
from habit_tracker.application.use_cases.create_graph import create_graph
from habit_tracker.application.use_cases.create_user import create_user
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph import Graph
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType
from habit_tracker.infrastructure.http.requests_pixela_gateway import (
    RequestsPixelaGateway,
)
from tests.integration.local_pixela_server import running_server, unused_base_url

CREDENTIALS = Credentials.of("jens-test", "abcdefgh12345")
GRAPH = Graph(GraphId("run1"), "Running", "km", GraphType.FLOAT, GraphColor.AJISAI)


def test_create_user_succeeds_when_the_server_answers_200() -> None:
    with running_server(200, "Success.") as server:
        response = create_user(RequestsPixelaGateway(server.base_url), CREDENTIALS)
    assert (response.status_code, response.is_success) == (200, True)


def test_create_user_sends_a_post_to_the_users_path() -> None:
    with running_server() as server:
        create_user(RequestsPixelaGateway(server.base_url), CREDENTIALS)
        request = server.requests[0]
    assert (request.method, request.path) == ("POST", "/v1/users")


def test_create_user_sends_a_json_content_type() -> None:
    with running_server() as server:
        create_user(RequestsPixelaGateway(server.base_url), CREDENTIALS)
        request = server.requests[0]
    assert request.headers["content-type"] == "application/json"


def test_create_user_sends_the_lecture_body() -> None:
    with running_server() as server:
        create_user(RequestsPixelaGateway(server.base_url), CREDENTIALS)
        body = server.requests[0].body
    assert body == {
        "token": "abcdefgh12345",
        "username": "jens-test",
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }


def test_create_user_returns_the_message_when_the_server_answers_409() -> None:
    with running_server(409, "This username is already taken.") as server:
        response = create_user(RequestsPixelaGateway(server.base_url), CREDENTIALS)
    assert (response.status_code, response.is_success, response.message) == (
        409,
        False,
        "This username is already taken.",
    )


def test_create_graph_sends_a_post_to_the_graphs_path() -> None:
    with running_server() as server:
        create_graph(RequestsPixelaGateway(server.base_url), CREDENTIALS, GRAPH)
        request = server.requests[0]
    assert (request.method, request.path) == ("POST", "/v1/users/jens-test/graphs")


def test_create_graph_sends_the_token_in_the_x_user_token_header() -> None:
    with running_server() as server:
        create_graph(RequestsPixelaGateway(server.base_url), CREDENTIALS, GRAPH)
        headers = server.requests[0].headers
    assert headers["x-user-token"] == "abcdefgh12345"


def test_create_graph_keeps_the_token_out_of_the_path_and_the_body() -> None:
    with running_server() as server:
        create_graph(RequestsPixelaGateway(server.base_url), CREDENTIALS, GRAPH)
        request = server.requests[0]
    assert "abcdefgh12345" not in request.path
    assert "abcdefgh12345" not in str(request.body)


def test_create_graph_sends_the_graph_body() -> None:
    with running_server() as server:
        create_graph(RequestsPixelaGateway(server.base_url), CREDENTIALS, GRAPH)
        body = server.requests[0].body
    assert body == {
        "id": "run1",
        "name": "Running",
        "unit": "km",
        "type": "float",
        "color": "ajisai",
    }


def test_create_graph_returns_the_message_when_the_server_answers_409() -> None:
    with running_server(409, "This graphID already exists.") as server:
        response = create_graph(
            RequestsPixelaGateway(server.base_url), CREDENTIALS, GRAPH
        )
    assert (response.status_code, response.is_success) == (409, False)


def test_gateway_raises_gateway_error_when_the_connection_is_refused() -> None:
    gateway = RequestsPixelaGateway(unused_base_url())
    with pytest.raises(GatewayError):
        create_user(gateway, CREDENTIALS)
