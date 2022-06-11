from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request')
def exercise_request():
    return f'Hello, {request.args.get("box")} .'