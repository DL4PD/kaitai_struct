<?php
namespace Kaitai\Struct\Tests;

class Expr2Test extends TestCase {
    public function testExpr2() {
        $r = Expr2::fromFile(self::SRC_DIR_PATH . "/str_encodings.bin");

        $this->assertEquals(10, $r->str1()->lenOrig());
        $this->assertEquals(7, $r->str1()->lenMod());
        $this->assertEquals("Some AS", $r->str1()->str());

        $this->assertEquals(7, $r->str1Len());
        $this->assertEquals(7, $r->str1LenMod());
        $this->assertEquals(0x49, $r->str1Byte1());
        $this->assertEquals(0x49, $r->str1Avg());
        $this->assertEquals("e", $r->str1Char5());

        $this->assertEquals(0x65, $r->str1Tuple5()->byte0());
        $this->assertEquals(0x20, $r->str1Tuple5()->byte1());
        $this->assertEquals(0x41, $r->str1Tuple5()->byte2());
        $this->assertEquals(0x30, $r->str1Tuple5()->avg());

        $this->assertEquals(0x65, $r->str2Tuple5()->byte0());
        $this->assertEquals(0x20, $r->str2Tuple5()->byte1());
        $this->assertEquals(0x41, $r->str2Tuple5()->byte2());
        $this->assertEquals(0x30, $r->str2Tuple5()->avg());
    }
}