from flask import Flask
app= Flask(__name__)

@app.route('/user')
def user():
	return ' <h1> Hello <h1>'

if __name__=='__main__':
	app.run(debug=True)