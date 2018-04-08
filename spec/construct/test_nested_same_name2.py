# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from nested_same_name2 import _schema

class TestNestedSameName2(unittest.TestCase):
    def test_nested_same_name2(self):
        r = _schema.parse_file('src/nested_same_name2.bin')
        self.assertEqual(r.version, 66)
        self.assertEqual(r.main_data.main_size, 2)
        self.assertEqual(r.main_data.foo.data1, b"\x11\x11\x11\x11")
        self.assertEqual(r.dummy.dummy_size, 3)
        self.assertEqual(r.dummy.foo.data2, b"\x22\x22\x22\x22\x22\x22")