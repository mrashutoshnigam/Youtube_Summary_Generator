# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'


import datetime
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)