from flask import Flask, request, render_template, jsonify

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

@app.route('/exercise_request/<box>')
def exercise_request(box):
    return f'Hello, {box} .'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/exercise')
def excersize():
    return f'{request.args.get("my_name")}さん、ようこそ'

@app.route('/try_rest', methods=["POST"])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    #print(type(request_json))
    
    #name = request_json['name']
    #print(name)

    for a in request_json['friends']:
        print(a)

    response_json = {"response_json" : request_json}
    return jsonify(response_json)