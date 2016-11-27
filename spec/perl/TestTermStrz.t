package spec::perl::TestTermStrz;

use strict;
use warnings;
use base qw(Test::Class);
use Test::More;
use TermStrz;

sub test_term_strz: Test(3) {
    my $r = TermStrz->from_file('src/term_strz.bin');

    is($r->s1(), 'foo', 'Equals');
    is($r->s2(), 'bar', 'Equals');
    is($r->s3(), '|baz@', 'Equals');
}

Test::Class->runtests;