# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from params_call_short import ParamsCallShort

class TestParamsCallShort(unittest.TestCase):
    def test_params_call_short(self):
        with ParamsCallShort.from_file('src/term_strz.bin') as r:
            self.assertEqual(r.buf1.body, u"foo|b")
            self.assertEqual(r.buf2.body, u"ar|ba")
            self.assertEqual(r.buf2.trailer, 122)