import unittest

from nested_types2 import NestedTypes2

class TestNestedTypes2(unittest.TestCase):
    def test_nested_types2(self):
        with NestedTypes2.from_file("src/fixed_struct.bin") as r:

            self.assertEqual(r.one.typed_at_root.value_b, 80)

            self.assertEqual(r.one.typed_here1.value_c, 65)

            self.assertEqual(r.one.typed_here1.typed_here.value_d, 67)
            self.assertEqual(r.one.typed_here1.typed_parent.value_cc, 75)
            self.assertEqual(r.one.typed_here1.typed_root.value_b, 45)

            self.assertEqual(r.one.typed_here2.value_cc, 49)

            self.assertEqual(r.two.value_b, -1)