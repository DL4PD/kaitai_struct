// Autogenerated from KST: please remove this line if doing any edits by hand!

package io.kaitai.struct.spec;

import io.kaitai.struct.testformats.ExprBytesCmp;
import org.testng.annotations.Test;
import static org.testng.Assert.*;
public class TestExprBytesCmp extends CommonSpec {
    @Test
    public void testExprBytesCmp() throws Exception {
        ExprBytesCmp r = ExprBytesCmp.fromFile(SRC_DIR + "fixed_struct.bin");

        assertEquals(r.one(), new byte[] { 80 });
        assertEquals(r.two(), new byte[] { 65, 67, 75 });
        assertIntEquals(r.isEq(), true);
        assertIntEquals(r.isNe(), false);
        assertIntEquals(r.isLt(), true);
        assertIntEquals(r.isGt(), false);
        assertIntEquals(r.isLe(), true);
        assertIntEquals(r.isGe(), false);
        assertIntEquals(r.isLt2(), false);
        assertIntEquals(r.isGt2(), true);
    }
}