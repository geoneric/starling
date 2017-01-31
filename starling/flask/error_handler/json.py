from flask import jsonify
from werkzeug.exceptions import HTTPException


def response(
        code,
        description):
    """
    Format a response

    :param int code: HTTP error code
    :param str description: Error message
    :return: Tuple of a wrapped JSON snippet and the error code
    :rtype: Tuple of :py:class:`flask.Response` containing a JSON snippet,
        and the error code

    The JSON snippet is formatted like this:

    .. code-block:: json

       {
           "status_code": 404,
           "message": "The requested URL was not found on the server"
       }
    """

    payload = jsonify({
        "status_code": code,
        "message": description
    })
    print(type(payload))

    return payload, code


def http_exception_error_handler(
        exception):
    """
    Handle HTTP exception

    :param werkzeug.exceptions.HTTPException exception: Raised exception

    A response is returned, as formatted by the :py:func:`response` function.
    """

    assert issubclass(type(exception), HTTPException), type(exception)
    assert hasattr(exception, "code")
    assert hasattr(exception, "description")

    return response(exception.code, exception.description)
