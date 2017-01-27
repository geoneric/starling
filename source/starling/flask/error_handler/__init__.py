"""
Error handling
"""
from . import error_code


def register(
        app):
    """
    Register all available error handlers

    :param flask.Flask app: Application instance
    """
    error_code.register(app)
