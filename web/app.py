from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
	#notes = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

	notes = ['The following content is provided under a Creative Commons license',
 'Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free',
 'To make a donation or to view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw',
 'mit',
 'edu',
 "WILLIAM BONVILLIAN: So today, we really kind of talk more about the system, the kind of third direct innovation factor, and then about these indirect factors that are important and significant, but not as powerful, I'd argue, as the direct factors"
	]

	return render_template('notes.html', notes=notes)
