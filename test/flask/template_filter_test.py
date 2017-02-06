from datetime import datetime
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

        # Aware time point.
        now_string = time_point.utc_now().isoformat()

        self.assertDoesNotRaise(format_time_point, now_string)

        string = format_time_point(now_string)

        self.assertDoesNotRaise(datetime.strptime, string,
            "%Y-%m-%dT%H:%M:%S")

        # Unaware time point.
        now_string = datetime.utcnow().isoformat()

        self.assertDoesNotRaise(format_time_point, now_string)

        string = format_time_point(now_string)

        self.assertDoesNotRaise(datetime.strptime, string,
            "%Y-%m-%dT%H:%M:%S")


    def test_format_uuid(self):

        uuid = "6b0bfe46-6c07-43b4-892d-79dd66af401a"

        self.assertRaises(ValueError, format_uuid, uuid, 0)
        self.assertRaises(ValueError, format_uuid, uuid, 1)
        self.assertRaises(ValueError, format_uuid, uuid, 2)
        self.assertRaises(ValueError, format_uuid, uuid, 3)
        self.assertDoesNotRaise(format_uuid, uuid, 4)

        self.assertEqual(format_uuid(uuid, 4), "6...")
        self.assertEqual(format_uuid(uuid, 5), "6b...")
        self.assertEqual(format_uuid(uuid, 10), "6b0bfe4...")
        self.assertEqual(format_uuid(uuid), format_uuid(uuid, 10))
        self.assertEqual(format_uuid(uuid, len(uuid)), uuid)
        self.assertEqual(format_uuid(uuid, len(uuid) + 1), uuid)
