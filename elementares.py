from flask import Flask, request
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/soma')
def soma():
    int_input_1 = request.args.get('arg1', type=int)
    int_input_2 = request.args.get('arg2', type=int)
    int_output = {'result': (int_input_1 + int_input_2)}
    return jsonify(int_output)


@app.route('/subtracao')
def subtraia():
    int_input_1 = request.args.get('arg1', type=int)
    int_input_2 = request.args.get('arg2', type=int)
    int_output = {'result': (int_input_1 - int_input_2)}
    return jsonify(int_output)


@app.route('/multiplicacao')
def multiplica():
    int_input_1 = request.args.get('arg1', type=int)
    int_input_2 = request.args.get('arg2', type=int)
    int_output = {'result': (int_input_1 * int_input_2)}
    return jsonify(int_output)


@app.route('/divisao')
def divide():
    int_input_1 = request.args.get('arg1', type=int)
    int_input_2 = request.args.get('arg2', type=int)
    int_output = {'result': (int_input_1 / int_input_2)}
    return jsonify(int_output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
