// Autogenerated from KST: please remove this line if doing any edits by hand!

var assert = require('assert');
var testHelper = require('testHelper');

testHelper('JsSignedRightShift', 'src/fixed_struct.bin', function(r, JsSignedRightShift) {
  assert.strictEqual(r.shouldBe40000000, 1073741824);
  assert.strictEqual(r.shouldBeA00000, 10485760);
});