"""@file local_pixela_server.py
@brief A local HTTP server that stands in for Pixela in offline tests.

It listens on 127.0.0.1 only, records every request and answers with a
configurable status and JSON message.
"""

import json
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

## @brief The loopback address the server binds to.
LOCAL_HOST = "127.0.0.1"


@dataclass(frozen=True, slots=True)
class RecordedRequest:
    """@brief One request received by the local server."""

    ## @brief The HTTP method.
    method: str

    ## @brief The request path, with the leading slash.
    path: str

    ## @brief The request headers, names in lower case.
    headers: dict[str, str]

    ## @brief The decoded JSON body, or None when the body was empty.
    body: Any


class LocalPixelaServer:
    """@brief A recording server with a configurable answer."""

    def __init__(self, status: int = 200, message: str = "Success.") -> None:
        """@brief Create the server and bind it to a free port.

        @param status The HTTP status code of the answer.
        @param message The Pixela message of the answer.
        """
        self.status = status
        self.message = message
        self.requests: list[RecordedRequest] = []
        self._server = ThreadingHTTPServer((LOCAL_HOST, 0), self._make_handler())
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)

    @property
    def base_url(self) -> str:
        """@brief The base URL that points at this server."""
        return f"http://{LOCAL_HOST}:{self._server.server_address[1]}/v1"

    def start(self) -> None:
        """@brief Start answering requests in a background thread."""
        self._thread.start()

    def stop(self) -> None:
        """@brief Stop the server and free the port."""
        self._server.shutdown()
        self._server.server_close()
        self._thread.join()

    def _make_handler(self) -> type[BaseHTTPRequestHandler]:
        """@brief Build the request handler bound to this server object.

        @return The handler class.
        """
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802 - name fixed by http.server
                length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(length)
                owner.requests.append(
                    RecordedRequest(
                        method="POST",
                        path=self.path,
                        headers={k.lower(): v for k, v in self.headers.items()},
                        body=json.loads(raw) if raw else None,
                    )
                )
                payload = json.dumps(
                    {
                        "message": owner.message,
                        "isSuccess": owner.status < 400,
                    }
                ).encode()
                self.send_response(owner.status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
                """Keep the test output quiet."""

        return Handler


@contextmanager
def running_server(
    status: int = 200, message: str = "Success."
) -> Iterator[LocalPixelaServer]:
    """@brief Run a local server for the length of a `with` block.

    @param status The HTTP status code of the answer.
    @param message The Pixela message of the answer.
    @return The running server.
    """
    server = LocalPixelaServer(status, message)
    server.start()
    try:
        yield server
    finally:
        server.stop()


def unused_base_url() -> str:
    """@brief Return a base URL on which nothing listens.

    @return A loopback URL whose port was just released.
    """
    with running_server() as server:
        url = server.base_url
    return url
