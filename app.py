from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	title = 'Privacypilot'
	return render_template('home.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
