"""@file test_graph_domain.py
@brief Unit tests of the graph value objects.
"""

import dataclasses

import pytest

from habit_tracker.domain.errors.invalid_input_error import InvalidInputError
from habit_tracker.domain.value_objects.graph import Graph
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType


def _graph(name: str = "Running", unit: str = "km") -> Graph:
    """@brief Build a graph with valid defaults."""
    return Graph(GraphId("run1"), name, unit, GraphType.FLOAT, GraphColor.AJISAI)


def test_graph_id_is_accepted_when_it_follows_the_rule() -> None:
    assert GraphId("run-1").value == "run-1"


def test_graph_id_str_is_the_text() -> None:
    assert str(GraphId("run1")) == "run1"


def test_graph_id_is_accepted_at_the_shortest_length() -> None:
    assert GraphId("ab").value == "ab"


def test_graph_id_is_accepted_at_the_longest_length() -> None:
    assert GraphId("a" * 17).value == "a" * 17


@pytest.mark.parametrize(
    "text", ["a", "a" * 18, "1abc", "-abc", "Abc", "ab_c", "ab c", ""]
)
def test_graph_id_is_rejected_when_it_breaks_the_rule(text: str) -> None:
    with pytest.raises(InvalidInputError):
        GraphId(text)


def test_graph_types_are_int_and_float() -> None:
    assert {t.value for t in GraphType} == {"int", "float"}


def test_graph_colors_are_exactly_the_six_pixela_names() -> None:
    assert [c.value for c in GraphColor] == [
        "shibafu",
        "momiji",
        "sora",
        "ichou",
        "ajisai",
        "kuro",
    ]


def test_graph_color_is_rejected_when_the_name_is_unknown() -> None:
    with pytest.raises(ValueError):
        GraphColor("red")


def test_graph_type_is_rejected_when_the_name_is_unknown() -> None:
    with pytest.raises(ValueError):
        GraphType("string")


def test_graph_is_accepted_when_all_parts_are_valid() -> None:
    assert _graph().name == "Running"


@pytest.mark.parametrize("name", ["", "   "])
def test_graph_is_rejected_when_the_name_is_empty(name: str) -> None:
    with pytest.raises(InvalidInputError):
        _graph(name=name)


@pytest.mark.parametrize("unit", ["", "   "])
def test_graph_is_rejected_when_the_unit_is_empty(unit: str) -> None:
    with pytest.raises(InvalidInputError):
        _graph(unit=unit)


def test_graph_is_immutable() -> None:
    with pytest.raises(dataclasses.FrozenInstanceError):
        _graph().name = "other"  # type: ignore[misc]  # frozen on purpose
