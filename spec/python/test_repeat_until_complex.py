import unittest

from repeat_until_complex import RepeatUntilComplex

class TestRepeatUntilComplex(unittest.TestCase):
    def test_repeat_until_complex(self):
        with RepeatUntilComplex.from_file("src/repeat_until_complex.bin") as r:

            self.assertEqual(len(r.first), 3)
            self.assertEqual(r.first[0].count, 4)
            self.assertEqual(r.first[0].values, [1, 2, 3, 4])
            self.assertEqual(r.first[1].count, 2)
            self.assertEqual(r.first[1].values, [1, 2])
            self.assertEqual(r.first[2].count, 0)
            self.assertEqual(r.first[2].values, [])

            self.assertEqual(len(r.second), 4)
            self.assertEqual(r.second[0].count, 6)
            self.assertEqual(r.second[0].values, [1, 2, 3, 4, 5, 6])
            self.assertEqual(r.second[1].count, 3)
            self.assertEqual(r.second[1].values, [1, 2, 3])
            self.assertEqual(r.second[2].count, 4)
            self.assertEqual(r.second[2].values, [1, 2, 3, 4])
            self.assertEqual(r.second[3].count, 0)
            self.assertEqual(r.second[3].values, [])

            self.assertEqual(r.third, [102, 111, 111, 98, 97, 114, 0])