from flask import Flask, request, render_template, redirect, flash, jsonify

from surveys import *

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "turtles"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def start_survey():
    return render_template("templates/start_survey.html", title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)
    

