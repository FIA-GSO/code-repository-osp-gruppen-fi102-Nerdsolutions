from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/")
def index():
    variable = 'variableee'
    var = "b"
    return render_template('index.html', **locals())
