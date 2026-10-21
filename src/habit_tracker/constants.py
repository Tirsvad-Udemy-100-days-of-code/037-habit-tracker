"""@file constants.py
@brief Constants of the Habit Tracker: Pixela endpoint, field names and settings.

Every constant of the project is defined here, once.
"""

## @brief Base URL of the Pixela API, version 1.
PIXELA_BASE_URL = "https://pixe.la/v1"

## @brief Path segment of the users resource.
USERS_PATH = "users"

## @brief Path segment of the graphs resource.
GRAPHS_PATH = "graphs"

## @brief Name of the HTTP header that carries the user token.
TOKEN_HEADER = "X-USER-TOKEN"

## @brief Name of the environment variable that holds the Pixela username.
ENV_USERNAME = "PIXELA_USERNAME"

## @brief Name of the environment variable that holds the Pixela token.
ENV_TOKEN = "PIXELA_TOKEN"

## @brief Format of a pixel date: four digit year, month and day, no separator.
DATE_FORMAT = "%Y%m%d"

## @brief Seconds to wait for the Pixela API before the request is given up.
REQUEST_TIMEOUT_SECONDS = 10

## @brief JSON field: the user token (create user).
FIELD_TOKEN = "token"

## @brief JSON field: the username (create user).
FIELD_USERNAME = "username"

## @brief JSON field: the terms of service were accepted (create user).
FIELD_AGREE_TERMS = "agreeTermsOfService"

## @brief JSON field: the user is not a minor (create user).
FIELD_NOT_MINOR = "notMinor"

## @brief JSON field: the graph identifier (create graph).
FIELD_GRAPH_ID = "id"

## @brief JSON field: the graph name (create graph).
FIELD_GRAPH_NAME = "name"

## @brief JSON field: the unit of measure of a graph (create graph).
FIELD_GRAPH_UNIT = "unit"

## @brief JSON field: the data type of a graph, int or float (create graph).
FIELD_GRAPH_TYPE = "type"

## @brief JSON field: the colour of a graph (create graph).
FIELD_GRAPH_COLOR = "color"

## @brief JSON field: the date of a pixel (post pixel).
FIELD_PIXEL_DATE = "date"

## @brief JSON field: the quantity of a pixel (post pixel).
FIELD_PIXEL_QUANTITY = "quantity"

## @brief Value that Pixela expects for a confirmed yes.
VALUE_YES = "yes"

## @brief Value that Pixela expects for a declined no.
VALUE_NO = "no"

## @brief Text printed instead of the token when a request is shown.
HIDDEN_TOKEN = "********"
