from starling import time_point
from test.test_case import TestCase
from starling.flask.template_filter import *


class TemplateFilterTest(TestCase):

    def test_format_pathname(self):

        self.assertRaises(ValueError, format_pathname, "bla", 0)
        self.assertRaises(ValueError, format_pathname, "bla", 1)
        self.assertRaises(ValueError, format_pathname, "bla", 2)
        self.assertRaises(ValueError, format_pathname, "bla", 3)
        self.assertDoesNotRaise(format_pathname, "bla", 4)

        self.assertEqual(format_pathname("blah", 10), "blah")
        self.assertEqual(format_pathname("/tmp/blah", 10), "/tmp/blah")
        self.assertEqual(format_pathname("/tmp/blaah", 10), "/tmp/blaah")
        self.assertEqual(format_pathname("/tmp/blaaah", 10), ".../blaaah")

    def test_format_time_point(self):

        now_string = time_point.utc_now().isoformat()

        self.assertDoesNotRaise(format_time_point, now_string)
