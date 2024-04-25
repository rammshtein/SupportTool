from flask import Flask
from datetime import datetime


app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

@app.route("/date")
def current_time():
    return "This page was served and updated at :" + str(datetime.now())

counter=0
@app.route("/count_views")
def count_views():
    global counter
    counter +=1
    return "This page show how many viewers this page get requested :" + str(counter) + " times."