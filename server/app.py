from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'test'

@app.route('/transcript')
def transcript():
	if request.method != 'POST':
		return 405

	return 'foo'
