from flask import flask

app = new flask(__name__)

@app.route("/")
def main_page():
    return "<H1>Hello world!</H1>"
