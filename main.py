from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/room1')
def room1():
    return render_template("room1.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')

