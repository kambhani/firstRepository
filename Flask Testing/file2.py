#How to add html files to Flask application
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    temp = "Sample text"
    return render_template("page2.html", temp = temp)

@app.route("/bye")
def bye():
    temp = "Adios"
    return render_template("page2.html", temp = temp)




