
import os

from flask import Flask, render_template, redirect, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
# from __init__ import app
# from models.lessons import menus, TITLE, PROJECTS, select_2_proj, lessons_dict
# import requests

from flask import Flask, render_template, request, url_for
# from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_name = db.Column(db.String(10), unique=False, nullable=False)
    p_score = db.Column(db.Integer, unique=False, nullable=False)  # want score as int so we can sort by it easily.

def __init__(self, p_name, p_score):
    self.p_name = p_name
    self.p_score = p_score

def __repr__(self):
    return f"{self.p_name},{self.p_score}"



# from tkinter import *

#Use of Routes here
#connects default URL of server to render home.html
@app.route('/')
def main():
    return render_template("home.html")

@app.route('/game1')
def room1():
    return render_template("game1.html")

@app.route('/game2')
def room2():
    return render_template("game2.html")

@app.route('/game3')
def L2Room1():
    return render_template("game3.html")

@app.route('/game4')
def L2Room2():
    return render_template("game4.html")


@app.route('/loadingpage')
def CharSelect():
    return render_template("loadingpage")

@app.route('/apcsp')
def apcsp():
    return render_template("apcsp.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template("apcsp.html")
    return render_template('apcsp.html', error=error)

@app.route('/register')
def register():
    return render_template("register.php")

db = SQLAlchemy(app)


# we're adding to table scores
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_name = db.Column(db.String(10), unique=False, nullable=False)
    p_score = db.Column(db.Integer, unique=False, nullable=False)  # want score as int so we can sort by it easily.

    def __init__(self, p_name, p_score):
        self.p_name = p_name
        self.p_score = p_score

    def __repr__(self):
        return f"{self.p_name},{self.p_score}"


# db.create_all(); #to initialize the tables in the db. Do not need after first initilization

@app.route('/index')
def index():
    # go to the score table and query it, order it by the score value descending, limit 5 and serve up all of those items I asked for as a list.
    results = {1, 2, 3, 4}
    scores = []

    for result in results:
        score_dict = {"name": "name", 'score': 'score'}
        scores.append(score_dict)

    return render_template('login.html', scores=scores)


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        name = request.form['name']
        # the code below confirmed I had the proper data. Now to add it to the db.
        print(name)
        print(score)
        # here for now, should go to scores eventually.
        return redirect(url_for('scores', username=name))

    return render_template("name.html")


@app.route('/scores', methods=['GET', 'POST'])

@app.route('/scores/<string:username>/', methods=['GET', 'POST'])
def scores(username=''):
    # does same code as front page. TODO: After you get this to work, refactor this into a function
    results = Score.query.order_by(desc('p_score')).limit(5).all()
    scores = []

    for result in results:
        score_dict = {'name': result.p_name, 'score': result.p_score}
        scores.append(score_dict)

    if username != '':
        print(username)
        # spacing in the filter_by argument very important
        nameResults = Score.query.filter_by(p_name=username).order_by(desc('p_score')).limit(5).all()
        nameScores = []

        for nameResult in nameResults:
            name_dict = {'name': nameResult.p_name, 'score': nameResult.p_score}
            nameScores.append(name_dict)

    else:
        print('no username')
        nameScores = []

    return render_template('scores.html', scores=scores, nameScores=nameScores, username=username)
