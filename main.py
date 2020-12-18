
#Use of flask Here
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)


#Use of Routes here
#connects default URL of server to render home.html
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/room1')
def room1():
    return render_template("room1.html")

@app.route('/room2')
def room2():
    return render_template("room2.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')

