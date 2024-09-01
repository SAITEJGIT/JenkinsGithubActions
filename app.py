from flask import Flask, jsonify, request,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greetings')
def hello():
    return jsonify(message="Hello, Sai!")

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
