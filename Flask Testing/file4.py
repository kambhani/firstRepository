#This file will demonstrate loops

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alex", "Bill", "Cynthia"]
    return render_template("page4.html", names = names)
