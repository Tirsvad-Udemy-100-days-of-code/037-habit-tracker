"""@file gateway_error.py
@brief The error raised when the Pixela API cannot be reached.
"""


class GatewayError(Exception):
    """@brief A request could not be sent or no answer came back.

    A refusal by Pixela (for example a taken username) is not an error: it is
    an `ApiResponse` that is not a success.
    """
