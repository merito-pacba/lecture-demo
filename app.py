from flask import Flask

app = new Flask(__name__)

@app.route("/")
def main_page():
    return "<H1>Hello world!</H1>"
