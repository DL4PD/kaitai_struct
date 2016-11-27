import unittest

from switch_manual_int_else import SwitchManualIntElse

class TestSwitchManualIntElse(unittest.TestCase):
    def test_switch_manual_int_else(self):
        with SwitchManualIntElse.from_file("src/switch_opcodes2.bin") as r:

            self.assertEqual(len(r.opcodes), 4)

            self.assertEqual(r.opcodes[0].code, 83)
            self.assertEqual(r.opcodes[0].body.value, "foo")

            self.assertEqual(r.opcodes[1].code, 88)
            self.assertEqual(r.opcodes[1].body.filler, 0x42)

            self.assertEqual(r.opcodes[2].code, 89)
            self.assertEqual(r.opcodes[2].body.filler, 0xcafe)

            self.assertEqual(r.opcodes[3].code, 73)
            self.assertEqual(r.opcodes[3].body.value, 7)