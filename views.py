
from flask import render_template, request, redirect, url_for, Flask
# from __init__ import app
# from models.lessons import menus, TITLE, PROJECTS, select_2_proj, lessons_dict
# import requests

# from flask import Flask, render_template, request, url_for
# from werkzeug.utils import redirect

app = Flask(__name__)

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
