import { expect } from 'chai';

describe('Basic Arithmetic with Chai', function () {
  it('should add two numbers correctly', function () {
    const sum = 2 + 3;
    expect(sum).to.equal(5); // Checks if the sum is 5
  });

  it('should subtract two numbers correctly', function () {
    const difference = 5 - 2;
    expect(difference).to.equal(3); // Checks if the difference is 3
  });

  it('should include a number in the array', function () {
    const arr = [1, 2, 3];
    expect(arr).to.include(2); // Check if array includes the value 2
  });
});
