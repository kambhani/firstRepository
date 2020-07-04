#This file demonstrates linking to other webpages

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page5-1.html")

@app.route("/more")
def more():
    return render_template("page5-2.html")
