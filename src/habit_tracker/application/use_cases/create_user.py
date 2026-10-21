"""@file create_user.py
@brief Use case: create a Pixela user (first step of the assignment).
"""

from habit_tracker.application.dto.api_response import ApiResponse
from habit_tracker.application.endpoints import users_path
from habit_tracker.application.ports.pixela_gateway import PixelaGateway
from habit_tracker.constants import (
    FIELD_AGREE_TERMS,
    FIELD_NOT_MINOR,
    FIELD_TOKEN,
    FIELD_USERNAME,
    VALUE_NO,
    VALUE_YES,
)
from habit_tracker.domain.value_objects.credentials import Credentials


def _yes_no(flag: bool) -> str:
    """@brief Write a flag the way Pixela expects it.

    @param flag The flag.
    @return `yes` or `no`.
    """
    return VALUE_YES if flag else VALUE_NO


def create_user(
    gateway: PixelaGateway,
    credentials: Credentials,
    agree_terms: bool = True,
    not_minor: bool = True,
) -> ApiResponse:
    """@brief Create a Pixela user with a POST request.

    @param gateway The port that sends the request.
    @param credentials The username and the token of the new user.
    @param agree_terms True when the user accepts the terms of service.
    @param not_minor True when the user is not a minor.
    @return The answer of Pixela. A refusal, such as a taken username, is a
    response that is not a success, not an exception.
    @throws GatewayError The request could not be sent.
    """
    body = {
        FIELD_TOKEN: credentials.token.value,
        FIELD_USERNAME: str(credentials.username),
        FIELD_AGREE_TERMS: _yes_no(agree_terms),
        FIELD_NOT_MINOR: _yes_no(not_minor),
    }
    return gateway.post(users_path(), body, {})
