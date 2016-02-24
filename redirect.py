from flask import redirect
from flask import Flask

app= Flask(__name__)

@app.route('/home')

def index():
	return redirect('www.google.com')

if __name__ == '__main__':
	app.run(debug=True)
