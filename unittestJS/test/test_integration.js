// test/integration_test.js
import * as chai from 'chai';
import chaiHttp from 'chai-http';

import app from '../server.js'; // Import the server
const { expect } = chai;

chai.use(chaiHttp);

describe('Integration Tests for User API', () => {
  // Test the GET /users endpoint
  it('should return all users', (done) => {
    chai
      .request(app)
      .get('/users')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('array');
        expect(res.body.length).to.be.greaterThan(0);
        done();
      });
  });

  // Test the POST /users endpoint
  it('should add a new user', (done) => {
    chai
      .request(app)
      .post('/users')
      .send({ name: 'Jane Doe' })
      .end((err, res) => {
        expect(res).to.have.status(201);
        expect(res.body).to.be.an('object');
        expect(res.body.name).to.equal('Jane Doe');
        done();
      });
  });

  // Test the GET /users/:id endpoint for a valid user
  it('should return a user by ID', (done) => {
    chai
      .request(app)
      .get('/users/1')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('object');
        expect(res.body.name).to.equal('John Doe');
        done();
      });
  });

  // Test the GET /users/:id endpoint for an invalid user
  it('should return 404 for a user not found', (done) => {
    chai
      .request(app)
      .get('/users/99')
      .end((err, res) => {
        expect(res).to.have.status(404);
        expect(res.body).to.be.an('object');
        expect(res.body.error).to.equal('User not found');
        done();
      });
  });
});
