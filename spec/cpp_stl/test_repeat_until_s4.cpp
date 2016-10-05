#include <boost/test/unit_test.hpp>

#include <repeat_until_s4.h>

#include <iostream>
#include <fstream>
#include <vector>

#include "helpers.h"

BOOST_AUTO_TEST_CASE(test_repeat_until_s4) {
    std::ifstream ifs("src/repeat_until_s4.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    repeat_until_s4_t* r = new repeat_until_s4_t(&ks);

    COMPARE_ARRAY(uint32_t, r->entries(), 0x42, 0x1337, -251658241, -1);
    BOOST_CHECK_EQUAL(r->afterall(), std::string("foobar"));

    delete r;
}