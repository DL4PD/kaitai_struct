local luaunit = require("luaunit")

require("str_literals2")

TestStrLiterals2 = {}

function TestStrLiterals2:test_str_literals2()
    local r = StrLiterals2:from_file("src/fixed_struct.bin")

    luaunit.assertEquals(r.dollar1, "$foo")
    luaunit.assertEquals(r.dollar2, "${foo}")
    luaunit.assertEquals(r.hash, "#{foo}")
    luaunit.assertEquals(r.at_sign, "@foo")
end
