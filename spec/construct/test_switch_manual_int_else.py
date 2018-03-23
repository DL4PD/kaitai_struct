# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from switch_manual_int_else import _schema

class TestSwitchManualIntElse(unittest.TestCase):
    def test_switch_manual_int_else(self):
        r = _schema.parse_file('src/switch_opcodes2.bin')
        self.assertEqual(len(r.opcodes), 4)
        self.assertEqual(r.opcodes[0].code, 83)
        self.assertEqual(r.opcodes[0].body.value, u"foo")
        self.assertEqual(r.opcodes[1].code, 88)
        self.assertEqual(r.opcodes[1].body.filler, 66)
        self.assertEqual(r.opcodes[2].code, 89)
        self.assertEqual(r.opcodes[2].body.filler, 51966)
        self.assertEqual(r.opcodes[3].code, 73)
        self.assertEqual(r.opcodes[3].body.value, 7)
