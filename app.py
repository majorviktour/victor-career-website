from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Victor!</p>"


if__name__ == "__main__";
    app.run(host="0.0.0.0", debug=True)