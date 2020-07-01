#To run, change cd to the folder this is in, then type: python -m flask run
#To stop running, type Ctrl + C
#This file shows whether the current date is Jan. 1

import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #get current date & time, then store it in a variable called now
    now = datetime.datetime.now()
    #create boolean variable that stores whether the current day is New Years
    new_year = now.month == 1 and now.day == 1
    return render_template("page3.html", new_year = new_year)





