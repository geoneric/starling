import unittest


class TestCase(unittest.TestCase):

    def assertDoesNotRaise(self,
            callable,
            *args):
        try:
            callable(*args)
        except Exception as exception:
            self.fail(
                "callable raised unexpected exception: {}".format(exception))
