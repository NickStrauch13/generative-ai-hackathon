#!/usr/local/bin/python3
from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from combined_yt_gpt import main_combined, get_difficulty_and_time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/generate_steps', methods=['POST'])
@cross_origin()
def generate():
    # get the query from main_combined
    query = request.json['query']
    response_steps, yt_link = main_combined(query)
    data = {'response': response_steps, 'yt_link': yt_link}
    return jsonify(data)

@app.route('/get_difficulty', methods=['GET'])
@cross_origin()
def difficulty():
    # get the cache file from main_combined
    difficulty, time = get_difficulty_and_time()
    data = {'difficulty': difficulty, "time": time}
    return jsonify(data)

@app.route('/example', methods=['GET'])
def example():
    data = {'message': 'This is an example response.'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


