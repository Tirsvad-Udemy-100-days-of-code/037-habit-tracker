"""@file __init__.py
@brief Habit Tracker: track a habit with the Pixela HTTP API.

The package follows the layers of Clean Architecture: domain, application,
infrastructure and presentation. The functions of the assignment are exported
here.
"""

from habit_tracker.application.use_cases.create_user import create_user

__all__ = ["create_user"]
