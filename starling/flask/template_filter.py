"""
Filters to be used in jinja2 templates
"""
from datetime import datetime
from ..time_point import *


def format_pathname(
        pathname,
        max_length):
    """
    Format a pathname

    :param str pathname: Pathname to format
    :param int max_length: Maximum length of result pathname (> 3)
    :return: Formatted pathname
    :rtype: str
    :raises ValueError: If *max_length* is not larger than 3

    This function formats a pathname so it is not longer than *max_length*
    characters. The resulting pathname is returned. It does so by replacing
    characters at the start of the *pathname* with three dots, if necessary.
    The idea is that the end of the *pathname* is the most important part
    to be able to identify the file.
    """
    if max_length <= 3:
        raise ValueError("max length must be larger than 3")

    if len(pathname) > max_length:
        pathname = "...{}".format(pathname[-(max_length-3):])

    return pathname


def format_time_point(
        time_point_string):

    """
    :param str time_point_string: String representation of a time point
        to format
    :return: Formatted time point
    :rtype: str
    :raises ValueError: If *time_point_string* is not formatted according to
        ISO 8601

    See :py:meth:`datetime.datetime.isoformat` function for supported formats.
    """
    # formats = [
    #     "%Y-%m-%dT%H:%M:%S+HH:MM",
    #     "%Y-%m-%dT%H:%M:%S.%f",
    #     "%Y-%m-%dT%H:%M:%S",
    # ]
    time_point = None

    if len(time_point_string) == 32 and time_point_string[29] == ':':
        # Python cannot parse its own generated isoformat() string...
        # We need to get rid of the semicolon.
        time_point_string = time_point_string[:29] + \
            time_point_string[30:]
        format = "%Y-%m-%dT%H:%M:%S.%f%z"

        try:
            time_point = datetime.strptime(time_point_string, format)
        except:
            pass
    else:

        format = "%Y-%m-%dT%H:%M:%S.%f"

        try:
            time_point = datetime.strptime(time_point_string, format)
        except:
            pass

    # TODO Handle other time formats.

    if time_point is None:
        raise ValueError(
            "time point must be formatted according to ISO 8601 "
            "('{}')".format(time_point_string))

    if not is_aware(time_point):
        time_point = make_aware(time_point)

    time_point = local_time_point(time_point)

    return time_point.strftime("%Y-%m-%dT%H:%M:%S")


def format_uuid(
        uuid,
        max_length=10):
    """
    Format a UUID string

    :param str uuid: UUID to format
    :param int max_length: Maximum length of result string (> 3)
    :return: Formatted UUID
    :rtype: str
    :raises ValueError: If *max_length* is not larger than 3

    This function formats a UUID so it is not longer than *max_length*
    characters. The resulting string is returned. It does so by replacing
    characters at the end of the *uuid* with three dots, if necessary.
    The idea is that the start of the *uuid* is the most important part
    to be able to identify the related entity.

    The default *max_length* is 10, which will result in a string
    containing the first 7 characters of the *uuid* passed in. Most of
    the time, such a string is still unique within a collection of UUIDs.
    """
    if max_length <= 3:
        raise ValueError("max length must be larger than 3")

    if len(uuid) > max_length:
        uuid = "{}...".format(uuid[0:max_length-3])

    return uuid
