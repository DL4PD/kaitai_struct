#include <boost/test/unit_test.hpp>

#include <nested_types2.h>

#include <iostream>
#include <fstream>
#include <vector>

BOOST_AUTO_TEST_CASE(test_nested_types2) {
    std::ifstream ifs("src/fixed_struct.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    nested_types2_t* r = new nested_types2_t(&ks);

    BOOST_CHECK_EQUAL(r->one()->typed_at_root()->value_b(), 80);

    BOOST_CHECK_EQUAL(r->one()->typed_here1()->value_c(), 65);

    BOOST_CHECK_EQUAL(r->one()->typed_here1()->typed_here()->value_d(), 67);
    BOOST_CHECK_EQUAL(r->one()->typed_here1()->typed_parent()->value_cc(), 75);
    BOOST_CHECK_EQUAL(r->one()->typed_here1()->typed_root()->value_b(), 45);

    BOOST_CHECK_EQUAL(r->one()->typed_here2()->value_cc(), 49);

    BOOST_CHECK_EQUAL(r->two()->value_b(), -1);

    delete r;
}