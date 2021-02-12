from views import app

if __name__ == "__main__":
    #runs the application on the repl development server
    views.app.run(debug=True, port='80', host='192.168.86.51')
    #192.168.86.51
    #127.0.0.1
