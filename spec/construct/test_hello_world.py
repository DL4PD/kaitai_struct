# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from hello_world import _schema

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        r = _schema.parse_file('src/fixed_struct.bin')
        self.assertEqual(r.one, 80)
