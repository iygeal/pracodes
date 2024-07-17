#!/usr/bin/python3
"""Module to implement test for JWT authentication"""

from flask import Flask, jsonify, session, request, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt


app = Flask(__name__)

@app.route("/protected", methods=["GET"])
def protected():
    return jsonify(logged_in_as=get_jwt_identity()), 200


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
