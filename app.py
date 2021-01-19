from flask import Flask, request, render_template, redirect, flash, jsonify

from surveys import *

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "turtles"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def start_survey():
    return render_template("start_survey.html", title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

@app.route("/questions/<int:question_num>")
def ask_question(question_num):
    # Check to make sure the user is accessing the correct question
    if question_num != len(responses):
        flash("You are trying to access in invalid page")
        return redirect(f"/questions/{len(responses)}")

    question = satisfaction_survey.questions[question_num].question
    choices = satisfaction_survey.questions[question_num].choices

    return render_template("questions.html", question=question, choices=choices)

@app.route("/answer", methods=["POST"])
def handle_answer():
    # Get the answer from the user and store it in responses
    answer = request.form['answer']
    responses.append(answer)

    #Check to see if the amount of questions has run out, if so redirect to thank you page
    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route("/complete")
def thank_you():
    return render_template("thank_you.html")

    