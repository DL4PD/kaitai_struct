local luaunit = require("luaunit")

require("enum_fancy")

TestEnumFancy = {}

function TestEnumFancy:test_enum_fancy()
    local r = EnumFancy:from_file("src/enum_0.bin")

    luaunit.assertEquals(r.pet_1, EnumFancy.Animal.cat)
    luaunit.assertEquals(r.pet_2, EnumFancy.Animal.chicken)
end