"""@file urls.py
@brief Build the URL of a request to the Pixela API.
"""


def join_url(base_url: str, path: str) -> str:
    """@brief Join the base URL and a path with exactly one slash.

    @param base_url The base URL of the API.
    @param path The path below it.
    @return The full URL.
    """
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"
