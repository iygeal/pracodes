from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/api/hello', methods=['GET'])
def hello():
    """
    A simple hello world API
    ---
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify(message="Hello, World!")


if __name__ == '__main__':
    app.run(debug=True)
