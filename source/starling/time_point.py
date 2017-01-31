"""
Utilities for handling date and time
"""
from datetime import datetime, timezone
from pytz import UTC
from tzlocal import get_localzone


def utc_now():
    """
    Return an aware :py:class:`datetime.datetime` instance of the current
    date and time, in UTC timezone

    :return: Current date and time, in UTC timezone
    :rtype: datetime.datetime
    """
    return datetime.now(timezone.utc)


def is_aware(
        time_point):
    """
    Return whether ``time_point`` is aware of the timezone
    """
    return time_point.tzinfo is not None and \
        time_point.utcoffset() is not None


def make_aware(
        time_point):
    """
    Return an aware time point

    :param datetime.datetime time_point: Unaware time point in UTC
    :return: Aware time point in UTC timezone
    :rtype: datetime.datetime
    """
    assert not is_aware(time_point)

    return time_point.replace(tzinfo=UTC)


def local_time_point(
        time_point):
    """
    Return a time point with the same UTC time as ``time_point``, but
    in the local time zone

    :param datetime.datetime time_point: Aware time point
    :return: Time point in local timezone
    :rtype: datetime.datetime
    """
    assert is_aware(time_point)

    return time_point.astimezone(get_localzone())
