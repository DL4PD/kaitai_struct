// Autogenerated from KST: please remove this line if doing any edits by hand!

package spec

import (
	"os"
	"testing"
	"github.com/kaitai-io/kaitai_struct_go_runtime/kaitai"
	. "test_formats"
	"github.com/stretchr/testify/assert"
)

func TestExprEnum(t *testing.T) {
	f, err := os.Open("../../src/term_strz.bin")
	if err != nil {
		t.Fatal(err)
	}
	s := kaitai.NewStream(f)
	var r ExprEnum
	err = r.Read(s, &r, &r)
	if err != nil {
		t.Fatal(err)
	}

	tmp1, err := r.ConstDog()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, ExprEnum_Animal__Dog, tmp1)
	tmp2, err := r.DerivedBoom()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, ExprEnum_Animal__Boom, tmp2)
	tmp3, err := r.DerivedDog()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, ExprEnum_Animal__Dog, tmp3)
}