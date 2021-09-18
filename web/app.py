from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/transcript')
def transcript():
	if request.method != 'POST':
		return 405

	return 'foo'
