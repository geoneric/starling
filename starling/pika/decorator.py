import json
import sys
import traceback
import requests


def notify_client(
        notifier_uri,
        client_id,
        status_code,
        message=None):
    """
    Notify the client of the result of handling a request

    The payload contains two elements:

    - client_id
    - result

    The *client_id* is the id of the client to notify. It is assumed
    that the notifier service is able to identify the client by this id
    and that it can pass the *result* to it.

    The *result* always contains a *status_code* element. In case the
    message passed in is not None, it will also contain a *message*
    element.

    In case the notifier service does not exist or returns an error,
    an error message will be logged to *stderr*.
    """
    payload = {
        "client_id": client_id,
        "result": {
            "response": {
                "status_code": status_code
            }
        }
    }

    if message is not None:
        payload["result"]["response"]["message"] = message

    response = requests.post(notifier_uri, json=payload)

    if response.status_code != 201:
        sys.stderr.write("failed to notify client: {}\n".format(payload))
        sys.stderr.flush()


def consume_message(
        method):
    """
    Decorator for methods handling requests from RabbitMQ

    The goal of this decorator is to perform the tasks common to all
    methods handling requests:

    - Log the raw message to *stdout*
    - Decode the message into a Python dictionary
    - Log errors to *stderr*
    - Signal the broker that we're done handling the request

    The method passed in will be called with the message body as a
    dictionary. It is assumed here that the message body is a JSON string
    encoded in UTF8.
    """

    def wrapper(
            self,
            channel,
            method_frame,
            header_frame,
            body):

        # Log the message
        sys.stdout.write("received message: {}\n".format(body))
        sys.stdout.flush()

        try:

            # Grab the data and call the method
            body = body.decode("utf-8")
            data = json.loads(body)
            method(self, data)

        except Exception as exception:

            # Log the error message
            sys.stderr.write("{}\n".format(traceback.format_exc()))
            sys.stderr.flush()


        # Signal the broker we are done
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    return wrapper


def consume_message_with_notify(
        notifier_uri_getter):
    """
    Decorator for methods handling requests from RabbitMQ

    This decorator builds on the :py:func:`consume_message` decorator. It extents
    it by logic for notifying a client of the result of handling the
    request.

    The *notifier_uri_getter* argument must be a callable which accepts
    *self* and returns the uri of the notifier service.
    """

    def consume_message_with_notify_decorator(
            method):

        @consume_message
        def wrapper(
                self,
                data):

            notifier_uri = notifier_uri_getter(self)
            client_id = data["client_id"]

            # Forward the call to the method and notify the client of the
            # result
            try:
                method(self, data)
                notify_client(notifier_uri, client_id, 200)
            except Exception as exception:
                notify_client(notifier_uri, client_id, 400, str(exception))
                raise

        return wrapper

    return consume_message_with_notify_decorator
