
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

@app.route('/room1')
def room1():
    return render_template("room1.html")

@app.route('/room2')
def room2():
    return render_template("room2.html")

@app.route('/L2Room1')
def L2Room1():
    return render_template("L2Room1.html")

@app.route('/L2Room2')
def L2Room2():
    return render_template("L2Room2.html")


@app.route('/loadingpage')
def CharSelect():
    return render_template("loadingpage")

# Route for handling the login page logic
@app.route('/')
def home():
    return render_template ('register.html')
    if request.form:
        username = users(username =request.form.get("username"))

@app.route('/register')
def register():
    return render_template("register.html")