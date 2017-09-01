package spec::perl::TestExprArray;

use strict;
use warnings;
use base qw(Test::Class);
use Test::More;
use ExprArray;

sub test_expr_array: Test(15) {
    my $r = ExprArray->from_file('src/expr_array.bin');

    is($r->aint_size(), 4, 'Equals');
    is($r->aint_first(), 7657765, 'Equals');
    is($r->aint_last(), 16272640, 'Equals');
    is($r->aint_min(), 49185, 'Equals');
    is($r->aint_max(), 1123362332, 'Equals');

    is($r->afloat_size(), 3, 'Equals');
    is($r->afloat_first(), -2.6839530254859364e-121, 'Equals');
    is($r->afloat_last(), -1.1103359815095273e-175, 'Equals');
    is($r->afloat_min(), -8.754689149998834e+288, 'Equals');
    is($r->afloat_max(), -1.1103359815095273e-175, 'Equals');

    is($r->astr_size(), 3, 'Equals');
    is($r->astr_first(), 'foo', 'Equals');
    is($r->astr_last(), 'baz', 'Equals');
    is($r->astr_min(), 'bar', 'Equals');
    is($r->astr_max(), 'foo', 'Equals');
}

Test::Class->runtests;