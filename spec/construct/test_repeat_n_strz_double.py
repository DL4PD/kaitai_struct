# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from repeat_n_strz_double import _schema

class TestRepeatNStrzDouble(unittest.TestCase):
    def test_repeat_n_strz_double(self):
        r = _schema.parse_file('src/repeat_n_strz.bin')
        self.assertEqual(r.qty, 2)
        self.assertEqual(r.lines1, [u"foo"])
        self.assertEqual(r.lines2, [u"bar"])
