# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from repeat_n_strz import _schema

class TestRepeatNStrz(unittest.TestCase):
    def test_repeat_n_strz(self):
        r = _schema.parse_file('src/repeat_n_strz.bin')
        self.assertEqual(r.qty, 2)
        self.assertEqual(r.lines, [u"foo", u"bar"])
