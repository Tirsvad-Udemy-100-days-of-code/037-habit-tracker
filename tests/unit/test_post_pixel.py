"""@file test_post_pixel.py
@brief Unit tests of the post pixel use case, with a fake gateway.
"""

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import date

from habit_tracker import post_pixel
from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.pixel import Pixel
from habit_tracker.domain.value_objects.pixel_date import PixelDate
from habit_tracker.domain.value_objects.quantity import Quantity

SECRET = "abcdefgh12345"
CREDENTIALS = Credentials.of("jens-test", SECRET)
GRAPH_ID = GraphId("cycling")
PIXEL = Pixel(PixelDate.parse("2026-10-22"), Quantity("9.74"))
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


def test_post_pixel_posts_to_the_pixels_path_of_the_graph() -> None:
    gateway = FakeGateway()
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, PIXEL)
    assert gateway.calls[0][0] == "users/jens-test/graphs/cycling"


def test_post_pixel_sends_date_and_quantity_as_strings() -> None:
    gateway = FakeGateway()
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, PIXEL)
    assert gateway.calls[0][1] == {"date": "20261022", "quantity": "9.74"}


def test_post_pixel_sends_the_compact_date_when_built_from_a_date() -> None:
    gateway = FakeGateway()
    pixel = Pixel(PixelDate(date(2026, 10, 22)), Quantity("1"))
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, pixel)
    assert gateway.calls[0][1]["date"] == "20261022"


def test_post_pixel_sends_the_token_in_the_header() -> None:
    gateway = FakeGateway()
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, PIXEL)
    assert gateway.calls[0][2] == {"X-USER-TOKEN": SECRET}


def test_post_pixel_keeps_the_token_out_of_the_path_and_the_body() -> None:
    gateway = FakeGateway()
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, PIXEL)
    path, body, _ = gateway.calls[0]
    assert SECRET not in path
    assert SECRET not in body.values()
    assert "token" not in body


def test_post_pixel_sends_one_request() -> None:
    gateway = FakeGateway()
    post_pixel(gateway, CREDENTIALS, GRAPH_ID, PIXEL)
    assert len(gateway.calls) == 1


def test_post_pixel_returns_a_failed_result_when_status_is_404() -> None:
    refused = ApiResponse(404, "Graph not found.", False)
    assert post_pixel(FakeGateway(refused), CREDENTIALS, GRAPH_ID, PIXEL) == refused
