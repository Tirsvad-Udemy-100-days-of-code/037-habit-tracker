"""@file test_cli.py
@brief End-to-end tests of the command line, from arguments to exit code.
"""

import runpy
import sys
from io import StringIO

import pytest

from habit_tracker.constants import (
    EXIT_INVALID,
    EXIT_OK,
    EXIT_REJECTED,
    EXIT_UNREACHABLE,
    PIXELA_BASE_URL,
)
from habit_tracker.presentation.cli import main
from tests.integration.local_pixela_server import running_server, unused_base_url

SECRET = "abcdefgh12345"
ENVIRON = {"PIXELA_USERNAME": "jens-test", "PIXELA_TOKEN": SECRET}


def _run(
    argv: list[str], environ: dict[str, str], base_url: str = PIXELA_BASE_URL
) -> tuple[int, str]:
    """@brief Run the program and return the exit code and the output."""
    out = StringIO()
    code = main(argv, environ, out, base_url)
    return code, out.getvalue()


def test_dry_run_returns_ok() -> None:
    code, _ = _run(["--dry-run", "create-user"], ENVIRON)
    assert code == EXIT_OK


def test_dry_run_prints_the_request() -> None:
    _, output = _run(["--dry-run", "create-user"], ENVIRON)
    assert "POST https://pixe.la/v1/users" in output
    assert '"username": "jens-test"' in output


def test_dry_run_hides_the_token() -> None:
    _, output = _run(["--dry-run", "create-user"], ENVIRON)
    assert SECRET not in output


def test_dry_run_sends_nothing() -> None:
    with running_server() as server:
        _run(["--dry-run", "create-user"], ENVIRON, server.base_url)
        assert server.requests == []


def test_dry_run_shows_yes_when_the_consent_flags_are_given() -> None:
    _, output = _run(
        ["--dry-run", "create-user", "--agree-terms", "--not-minor"], ENVIRON
    )
    assert '"agreeTermsOfService": "yes"' in output
    assert '"notMinor": "yes"' in output


def test_dry_run_shows_no_when_the_consent_flags_are_missing() -> None:
    _, output = _run(["--dry-run", "create-user"], ENVIRON)
    assert '"agreeTermsOfService": "no"' in output


def test_missing_environment_variable_returns_invalid() -> None:
    code, output = _run(["create-user"], {"PIXELA_USERNAME": "jens-test"})
    assert code == EXIT_INVALID
    assert "PIXELA_TOKEN" in output


def test_invalid_token_returns_invalid() -> None:
    code, _ = _run(["create-user"], {**ENVIRON, "PIXELA_TOKEN": "short"})
    assert code == EXIT_INVALID


def test_invalid_token_is_never_printed() -> None:
    _, output = _run(["create-user"], {**ENVIRON, "PIXELA_TOKEN": "bad token"})
    assert "bad token" not in output


def test_invalid_username_returns_invalid_and_sends_nothing() -> None:
    with running_server() as server:
        code, _ = _run(
            ["create-user"],
            {**ENVIRON, "PIXELA_USERNAME": "Bad Name"},
            server.base_url,
        )
        assert (code, server.requests) == (EXIT_INVALID, [])


def test_create_user_returns_ok_when_the_server_accepts() -> None:
    with running_server(200, "Success.") as server:
        code, output = _run(["create-user"], ENVIRON, server.base_url)
    assert code == EXIT_OK
    assert "Success (200): Success." in output


def test_create_user_returns_rejected_when_the_server_answers_409() -> None:
    with running_server(409, "This username is already taken.") as server:
        code, output = _run(["create-user"], ENVIRON, server.base_url)
    assert code == EXIT_REJECTED
    assert "Rejected (409): This username is already taken." in output


def test_create_user_output_never_contains_the_token() -> None:
    with running_server() as server:
        _, output = _run(["create-user"], ENVIRON, server.base_url)
    assert SECRET not in output


GRAPH_ARGS = ["create-graph", "--id", "run1", "--name", "Running", "--unit", "km"]


def test_create_graph_dry_run_prints_the_request() -> None:
    code, output = _run(["--dry-run", *GRAPH_ARGS], ENVIRON)
    assert code == EXIT_OK
    assert "POST https://pixe.la/v1/users/jens-test/graphs" in output
    assert '"id": "run1"' in output
    assert '"color": "ajisai"' in output
    assert '"type": "float"' in output


def test_create_graph_dry_run_hides_the_token() -> None:
    _, output = _run(["--dry-run", *GRAPH_ARGS], ENVIRON)
    assert SECRET not in output


def test_create_graph_dry_run_shows_the_header_masked() -> None:
    _, output = _run(["--dry-run", *GRAPH_ARGS], ENVIRON)
    assert "X-USER-TOKEN: ********" in output


def test_create_graph_returns_ok_when_the_server_accepts() -> None:
    with running_server(200, "Success.") as server:
        code, output = _run(GRAPH_ARGS, ENVIRON, server.base_url)
        request = server.requests[0]
    assert code == EXIT_OK
    assert "Success (200): Success." in output
    assert request.headers["x-user-token"] == SECRET


def test_create_graph_returns_rejected_when_the_server_answers_409() -> None:
    with running_server(409, "This graphID already exists.") as server:
        code, output = _run(GRAPH_ARGS, ENVIRON, server.base_url)
    assert code == EXIT_REJECTED
    assert "Rejected (409): This graphID already exists." in output


def test_create_graph_output_never_contains_the_token() -> None:
    with running_server() as server:
        _, output = _run(GRAPH_ARGS, ENVIRON, server.base_url)
    assert SECRET not in output


def test_create_graph_returns_invalid_and_sends_nothing_when_id_is_invalid() -> None:
    args = ["create-graph", "--id", "Bad Id", "--name", "Running", "--unit", "km"]
    with running_server() as server:
        code, output = _run(args, ENVIRON, server.base_url)
        assert (code, server.requests) == (EXIT_INVALID, [])
    assert "graph id" in output


def test_create_graph_returns_invalid_and_sends_nothing_when_name_is_empty() -> None:
    args = ["create-graph", "--id", "run1", "--name", " ", "--unit", "km"]
    with running_server() as server:
        code, _ = _run(args, ENVIRON, server.base_url)
        assert (code, server.requests) == (EXIT_INVALID, [])


def test_create_graph_exits_with_two_and_sends_nothing_when_color_is_unknown() -> None:
    with running_server() as server:
        with pytest.raises(SystemExit) as info:
            _run([*GRAPH_ARGS, "--color", "red"], ENVIRON, server.base_url)
        assert (info.value.code, server.requests) == (EXIT_INVALID, [])


def test_create_graph_exits_with_two_and_sends_nothing_when_type_is_unknown() -> None:
    with running_server() as server:
        with pytest.raises(SystemExit) as info:
            _run([*GRAPH_ARGS, "--type", "string"], ENVIRON, server.base_url)
        assert (info.value.code, server.requests) == (EXIT_INVALID, [])


def test_create_graph_sends_the_chosen_type_and_color() -> None:
    args = [*GRAPH_ARGS, "--type", "int", "--color", "kuro"]
    with running_server() as server:
        _run(args, ENVIRON, server.base_url)
        body = server.requests[0].body
    assert (body["type"], body["color"]) == ("int", "kuro")


PIXEL_ARGS = [
    "post-pixel",
    "--graph-id",
    "cycling",
    "--date",
    "2026-10-22",
    "--quantity",
    "9.74",
]


def test_post_pixel_dry_run_prints_the_request() -> None:
    code, output = _run(["--dry-run", *PIXEL_ARGS], ENVIRON)
    assert code == EXIT_OK
    assert "POST https://pixe.la/v1/users/jens-test/graphs/cycling" in output
    assert '"date": "20261022"' in output
    assert '"quantity": "9.74"' in output


def test_post_pixel_dry_run_masks_the_token() -> None:
    _, output = _run(["--dry-run", *PIXEL_ARGS], ENVIRON)
    assert SECRET not in output
    assert "X-USER-TOKEN: ********" in output


def test_post_pixel_returns_ok_when_the_server_accepts() -> None:
    with running_server(200, "Success.") as server:
        code, output = _run(PIXEL_ARGS, ENVIRON, server.base_url)
        request = server.requests[0]
    assert code == EXIT_OK
    assert "Success (200): Success." in output
    assert request.headers["x-user-token"] == SECRET
    assert request.body == {"date": "20261022", "quantity": "9.74"}


def test_post_pixel_returns_rejected_when_the_server_answers_404() -> None:
    with running_server(404, "Graph not found.") as server:
        code, output = _run(PIXEL_ARGS, ENVIRON, server.base_url)
    assert code == EXIT_REJECTED
    assert "Rejected (404): Graph not found." in output


def test_post_pixel_output_never_contains_the_token() -> None:
    with running_server() as server:
        _, output = _run(PIXEL_ARGS, ENVIRON, server.base_url)
    assert SECRET not in output


def test_post_pixel_returns_invalid_and_sends_nothing_when_date_is_invalid() -> None:
    args = ["post-pixel", "--graph-id", "cycling", "--date", "2026-13-40"]
    with running_server() as server:
        code, output = _run([*args, "--quantity", "1"], ENVIRON, server.base_url)
        assert (code, server.requests) == (EXIT_INVALID, [])
    assert "date" in output


def test_post_pixel_returns_invalid_and_sends_nothing_when_quantity_is_text() -> None:
    args = ["post-pixel", "--graph-id", "cycling", "--date", "2026-10-22"]
    with running_server() as server:
        code, output = _run([*args, "--quantity", "abc"], ENVIRON, server.base_url)
        assert (code, server.requests) == (EXIT_INVALID, [])
    assert "quantity" in output


def test_post_pixel_returns_invalid_and_sends_nothing_when_graph_id_is_bad() -> None:
    args = ["post-pixel", "--graph-id", "Bad Id", "--date", "2026-10-22"]
    with running_server() as server:
        code, _ = _run([*args, "--quantity", "1"], ENVIRON, server.base_url)
        assert (code, server.requests) == (EXIT_INVALID, [])


def test_all_three_commands_return_ok_in_dry_run_mode_in_sequence() -> None:
    sequence = [["create-user"], GRAPH_ARGS, PIXEL_ARGS]
    codes = [_run(["--dry-run", *argv], ENVIRON)[0] for argv in sequence]
    assert codes == [EXIT_OK, EXIT_OK, EXIT_OK]


def test_unreachable_server_returns_unreachable() -> None:
    code, output = _run(["create-user"], ENVIRON, unused_base_url())
    assert code == EXIT_UNREACHABLE
    assert SECRET not in output


def test_main_writes_to_standard_output_when_no_stream_is_given() -> None:
    assert main(["--dry-run", "create-user"], ENVIRON) == EXIT_OK


def test_module_entry_point_exits_with_the_exit_code(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(sys, "argv", ["habit_tracker", "--dry-run", "create-user"])
    monkeypatch.setenv("PIXELA_USERNAME", "jens-test")
    monkeypatch.setenv("PIXELA_TOKEN", SECRET)
    with pytest.raises(SystemExit) as info:
        runpy.run_module("habit_tracker", run_name="__main__")
    assert info.value.code == EXIT_OK
