from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000