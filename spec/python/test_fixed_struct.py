import unittest

from fixed_struct import FixedStruct

class TestFixedStruct(unittest.TestCase):
    def test_fixed_struct(self):
        r = FixedStruct.from_file('src/fixed_struct.bin')

        self.assertEqual(r.hdr.uint8, 255)
        self.assertEqual(r.hdr.uint16, 65535)
        self.assertEqual(r.hdr.uint32, 4294967295)
        self.assertEqual(r.hdr.uint64, 18446744073709551615)

        self.assertEqual(r.hdr.sint8, -1)
        self.assertEqual(r.hdr.sint16, -1)
        self.assertEqual(r.hdr.sint32, -1)
        self.assertEqual(r.hdr.sint64, -1)

        self.assertEqual(r.hdr.uint16le, 66)
        self.assertEqual(r.hdr.uint32le, 66)
        self.assertEqual(r.hdr.uint64le, 66)

        self.assertEqual(r.hdr.sint16le, -66)
        self.assertEqual(r.hdr.sint32le, -66)
        self.assertEqual(r.hdr.sint64le, -66)

        self.assertEqual(r.hdr.uint16be, 66)
        self.assertEqual(r.hdr.uint32be, 66)
        self.assertEqual(r.hdr.uint64be, 66)

        self.assertEqual(r.hdr.sint16be, -66)
        self.assertEqual(r.hdr.sint32be, -66)
        self.assertEqual(r.hdr.sint64be, -66)

        r.close()