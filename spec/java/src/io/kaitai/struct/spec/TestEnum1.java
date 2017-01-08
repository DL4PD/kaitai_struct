package io.kaitai.struct.spec;

import io.kaitai.struct.testformats.Enum1;
import org.testng.annotations.Test;

import static org.testng.Assert.assertEquals;

public class TestEnum1 extends CommonSpec {
    @Test
    public void testEnum1() throws Exception {
        Enum1 r = Enum1.fromFile(SRC_DIR + "enum_0.bin");

        assertEquals(r.main().submain().pet1(), Enum1.MainObj.Animal.CAT);
        assertEquals(r.main().submain().pet2(), Enum1.MainObj.Animal.CHICKEN);
    }
}