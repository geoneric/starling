"""
Utilities for handling date and time
"""
from datetime import datetime, timezone


def utc_now():
    """
    Return an aware :py:class:`datetime.datetime` instance of the current
    date and time, in UTC timezone

    :return: Current date and time, in UTC timezone
    :rtype: datetime.datetime
    """
    return datetime.now(timezone.utc)
