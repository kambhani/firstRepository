#This file demonstrates forms with Flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("page7-1.html")

@app.route("/hello", methods=["Get", "POST"])
def hello():
    if request.method == "GET":
        return "Plz submit da form"
    else:
        name = request.form.get("name")
        return render_template("page7-2.html", name = name)