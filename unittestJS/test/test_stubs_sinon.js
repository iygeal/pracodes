import sinon from 'sinon';
import { expect } from 'chai';

// Example module that makes API call
const userService = {
  fetchUserData: function (userId) {
    // Simulate fetching user data fro an API
    return fetch(`https://api.example./com/users/${userId}`)
      .then((response) => response.json())
      .then((data) => data);
  },
};

describe('User Service Tests', function () {
  it('should return stibbed user dta', async function () {
    const stub = sinon.stub(userService, 'fetchUserData');

    // Define the stub to return fake user data
    stub.withArgs(1).resolves({ id: 1, name: 'John Doe' });

    const result = await userService.fetchUserData(1); // call stubbed verssion

    expect(result).to.deep.equal({ id: 1, name: 'John Doe' }); // Tesk fake data

    stub.restore(); // Restore the original function
  });
});
