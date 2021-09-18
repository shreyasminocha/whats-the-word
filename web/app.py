import os

from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTS = ['srt', 'txt']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
	file = request.files['transcript']

	if file.filename == '':
		return render_template('notes.html', notes=[]), 400

	permitted_file = ('.' in file.filename) and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS
	if not permitted_file:
		return render_template('notes.html', notes=[]), 400

	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	notes = ['The following content is provided under a Creative Commons license',
		'Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free',
		'To make a donation or to view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw',
		'mit',
		'edu',
		"WILLIAM BONVILLIAN: So today, we really kind of talk more about the system, the kind of third direct innovation factor, and then about these indirect factors that are important and significant, but not as powerful, I'd argue, as the direct factors"
	]

	return render_template('notes.html', notes=notes)
