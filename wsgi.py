from views import app



'''
if __name__ == "__main__":
    #runs the application on the repl development server
    #app.run(debug=True, port='8080', host='127.0.0.1')
    #192.168.86.51
    #127.0.0.1
	#remove comment from line 5, comment the line below. If that works for you.
	app.run(debug=True)

'''

# RUNv
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5042')

