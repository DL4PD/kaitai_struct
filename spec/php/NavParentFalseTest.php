<?php
namespace Kaitai\Struct\Tests;

class NavParentFalseTest extends TestCase {
    public function testNavParentFalse() {
        $r = NavParentFalse::fromFile(self::SRC_DIR_PATH . "/nav_parent_codes.bin");

        $this->assertEquals(3, $r->childSize);
        $this->assertEquals(73, $r->elementA->foo->code);
        $this->assertEquals("123", $r->elementA->foo->more);
        $this->assertEquals(66, $r->elementA->bar->foo->code);
        $this->assertEquals(98, $r->elementB->foo->code);
    }
}