#To run, change cd to the folder this is in, then type: python -m flask run
#To stop running, type Ctrl + C
#To prevent me from using a lot of folders, I will type a lot of testing into this file, using comments as necessary

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Helloooo, {name}!!!</h1>"




