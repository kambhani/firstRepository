#This file demonstrates template inheritance

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page6-2.html")

@app.route("/more")
def more():
    return render_template("page6-3.html")
