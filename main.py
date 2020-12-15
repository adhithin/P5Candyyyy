
#Use of flask Here
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)


#Use of Routes here
#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(port='3000', host='0.0.0.0')
