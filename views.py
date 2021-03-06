import os
from flask import Flask, render_template, redirect, url_for
from flask import request



from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
# from __init__ import app
#from models.lessons import menus, TITLE, PROJECTS, select_2_proj, lessons_dict
# import requests

from flask import Flask, render_template, request, url_for
# from werkzeug.utils import redirect

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_name = db.Column(db.String(10), unique=False, nullable=False)
    p_score = db.Column(db.Integer, unique=False, nullable=False) # want score as int so we can sort by it easily.
    p_game = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, p_name, p_score, p_game):
        self.p_name = p_name
        self.p_score = p_score
        self.p_game = p_game

    def __repr__(self):
        return f"{self.p_name},{self.p_score}, {self.p_game}"

#code for the ratings table
db.create_all();

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_name = db.Column(db.String(10), unique=False, nullable=False)
    p_rating = db.Column(db.Integer, unique=False, nullable=False) # want score as int so we can sort by it easily.
    p_commment = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, p_name, p_rating, p_commment):
        self.p_name = p_name
        self.p_rating = p_rating
        self.p_commment = p_commment

    def __repr__(self):
        return f"{self.p_name},{self.p_rating}, {self.p_commment}"

#must go after 'models'
db.create_all();


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/ratings", methods=['GET', 'POST'])
def ratings():

    if request.method == 'POST':
        name = request.form['name']
        rating = int(request.form['rating'])
        comment = request.form['comment']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(name)
        print(rating)
        print(comment)

        new_review = Rating(name, rating, comment)
        db.session.add(new_review)
        db.session.commit()

    #query the db for the ratings:
    results = Rating.query.order_by(desc('p_rating')).all()
    arcade_ratings = []

    for result in results:
        rating_dict = {'name':result.p_name, 'rating':result.p_rating, 'comment':result.p_commment}
        arcade_ratings.append(rating_dict)

    return render_template('ratings.html', arcade_ratings = arcade_ratings)




@app.route('/game1', methods=['GET', 'POST'])
def game1():
    gameScores='nothing'
    print('game1 views.py')

    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        game = request.form['game']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(Score(name, score, game))

        new_score = Score(name, score, game)
        db.session.add(new_score)
        db.session.commit()

        #query the db for the relevant scores on this table:
        gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
        gameScores = []

        for gameResult in gameResults:
            game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
            gameScores.append(game_dict)

    #return redirect(url_for('game1', gameScores=gameScores))

    return render_template('game1-1.html', gameScores=gameScores)


@app.route('/game3', methods=['GET', 'POST'])
def game3():
    gameScores='nothing'

    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        game = request.form['game']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(Score(name, score, game))

        new_score = Score(name, score, game)
        db.session.add(new_score)
        db.session.commit()

        #query the db for the relevant scores on this table:
        gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
        gameScores = []

        for gameResult in gameResults:
            game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
            gameScores.append(game_dict)

    return render_template('game3.html', gameScores=gameScores)

# from tkinter import *

#Use of Routes here
#connects default URL of server to render home.html

@app.route('/game2', methods=['GET', 'POST'])
def game2():
    gameScores='nothing'

    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        game = request.form['game']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(Score(name, score, game))

        new_score = Score(name, score, game)
        db.session.add(new_score)
        db.session.commit()

        #query the db for the relevant scores on this table:
        gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
        gameScores = []

        for gameResult in gameResults:
            game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
            gameScores.append(game_dict)

    return render_template('game2.html', gameScores=gameScores)


@app.route('/game4', methods=['GET', 'POST'])
def game4():
    gameScores='nothing'
    print('game4 views.py')

    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        game = request.form['game']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(Score(name, score, game))

        new_score = Score(name, score, game)
        db.session.add(new_score)
        db.session.commit()

        #query the db for the relevant scores on this table:
        gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
        gameScores = []

        for gameResult in gameResults:
            game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
            gameScores.append(game_dict)

    return render_template('game4.html', gameScores=gameScores)
#    return render_template("game4.html")

@app.route('/game6', methods=['GET', 'POST'])
def game6():
    gameScores='nothing'
    print('game6 views.py')

    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        game = request.form['game']
        #the code below confirmed I had the proper data. Now to add it to the db.
        print(Score(name, score, game))

        new_score = Score(name, score, game)
        db.session.add(new_score)
        db.session.commit()

        #query the db for the relevant scores on this table:
        gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
        gameScores = []

        for gameResult in gameResults:
            game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
            gameScores.append(game_dict)

    return render_template('game6.html', gameScores=gameScores)
#    return render_template("game6.html")

@app.route('/game7')
def game7():
    return render_template("game7.html")

@app.route('/game8')
def game8():
    return render_template("game8.html")


@app.route('/apcsp')
def apcsp():
    return render_template("apcsp.html")

@app.route('/apcsp/adhithi')
def adhithi():
    return render_template("adhithi.html")

@app.route('/pedro')
def pedro():
    return render_template("pedro.html")

@app.route('/arul')
def arul():
    return render_template("arul.html")

@app.route('/akhil')
def akhilesh():
    return render_template("akhil.html")



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