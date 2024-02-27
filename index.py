from flask import Flask, render_template, request, jsonify

from model import authenticate

app = Flask(__name__)


@app.route("/login")
def login():
    return render_template('login.html')


def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Invalid username or password'}), 400

    user = authenticate(username, password)
    if user:
        return jsonify({'message': 'Login successful', 'user_id': user.id})
    else:
        return jsonify({'error': 'Authentication failed'}), 401


if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
def index():
    variable = 'Nur eine Test-'
    var = "Seite"
    return render_template('index.html', **locals())
