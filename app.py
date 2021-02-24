import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
#import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

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

#must go after 'models'
db.create_all();

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/game1', methods=['GET', 'POST'])
def game1():
	gameScores='nothing'
	print('game1 app.py')

	if request.method == 'POST':
		name = request.form['name']
		score = int(request.form['score'])
		game = request.form['game']
		#the code below confirmed I had the proper data. Now to add it to the db.
		#print(Score(name, score, game))

		new_score = Score(name, score, game)
		db.session.add(new_score)
		db.session.commit()

		#query the db for the relevant scores on this table:
		gameResults = Score.query.filter_by(p_game=game).order_by('p_score').all()
		gameScores = []

		for gameResult in gameResults:
			game_dict = {'name':gameResult.p_name, 'score':gameResult.p_score}
			gameScores.append(game_dict)

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

#moved this down to see if it was interfering with game3
@app.route('/leaderboard')
def index():
	# go to the score table and query it, order it by the score value descending, limit 5 and serve up all of those items I asked for as a list.
	results = {1, 2, 3, 4}
	scores = []

	for result in results:
		score_dict = {"name": "name", 'score': 'score', "game":"game"}
		scores.append(score_dict)

		return render_template('leaderboard.html', scores=scores)



@app.route('/apcsp')
def apcsp():
	return render_template('apcsp.html')

@app.route("/ratings", methods=['GET', 'POST'])
def ratings():
	gameScores='nothing'

	if request.method == 'POST':
		name = request.form['name']
		score = request.form['score']
		game = request.form['rating']
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

	return render_template('ratings.html', gameScores=gameScores)

@app.route('/index')
def game5():
	return render_template('index.html')

@app.route('/apcsp/adhithi')
def adhithi():
	return render_template('adhithi.html')
