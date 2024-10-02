const assert = require('assert');

// Group tests using describe
describe('Array', function () {
  // Individual test case
  it('should return -1 when the value is not present', function () {
    assert.strictEqual([1, 2, 3].indexOf(4), -1);
  });

  // Another test case
  it('should return the index when the value is present', function () {
    assert.strictEqual([1, 2, 3].indexOf(1), 0);
  });
});
