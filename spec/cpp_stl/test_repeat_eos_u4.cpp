#include <boost/test/unit_test.hpp>

#include <repeat_eos_u4.h>

#include <iostream>
#include <fstream>
#include <vector>

#include "helpers.h"

BOOST_AUTO_TEST_CASE(test_repeat_eos_u4) {
    std::ifstream ifs("src/repeat_eos_struct.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    repeat_eos_u4_t* r = new repeat_eos_u4_t(&ks);

    COMPARE_ARRAY(uint32_t, r->numbers(), 0, 0x42, 0x42, 0x815);

    delete r;
}