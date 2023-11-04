#!/usr/local/bin/python3

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    pass

@app.route('/example', methods=['GET'])
def example():
    data = {'message': 'This is an example response.'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


