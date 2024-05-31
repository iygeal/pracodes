#!/usr/bin/python3
"""Testing route in flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/name/<name>')
def greeting(name):
    """Greetings to name"""
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)
