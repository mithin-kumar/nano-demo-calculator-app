from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('calculator/greeting', methods=['GET'])
def greet():
    return 'Hello world!'


@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Missing parameters'}), 400

    num1 = data['first']
    num2 = data['second']

    try:
        result = float(num1) + float(num2)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'second' not in data or 'first' not in data:
        return jsonify({'error': 'Missing parameters'}), 400

    num1 = data['first']
    num2 = data['second']

    try:
        result = float(num1) - float(num2)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400


if __name__ == '__main__':
    app.run(debug=True)
