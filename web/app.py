import os

from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

#import sys

#print(sys.path())

#sys.path.append('./')

from Output import Output

ALLOWED_EXTS = ['srt', 'txt', 'mp3']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
	# has_transcript_file = True
	# has_audio_file = True

	# has_transcript_file = request.files['transcript']
	# has_audio_file = request.files['audio_file']
	# print("has_transcript_file", has_transcript_file)
	# print("has_audio_file", has_audio_file)

	has_transcript_file = 'transcript_file' in request.files.keys()
	has_audio_file = 'audio_file' in request.files.keys()

	print("has_transcript_file", has_transcript_file)
	print("has_audio_file", has_audio_file)

	if has_transcript_file:
		file = request.files['transcript_file']
	else:
		file = request.files['audio_file']
	
	print("request.files", request.files)

	# for key in request.files.keys():
	# 	print("request.files.keys item=", key)

	#print("app notes run()");

	#print("request.files['audio_file']");

	print("file.filename=", file.filename)

	if file.filename == '':
		return render_template('notes.html', notes=[]), 400

	permitted_file = ('.' in file.filename) and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS
	if not permitted_file:
		return render_template('notes.html', notes=[]), 400

	filename = secure_filename(file.filename)
	path_to_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	file.save(path_to_file)

	# Create a object of Class Output
	output_obj = Output()

	if has_transcript_file:
		output_obj.set_sentences_using_srt_path(path_to_file)
	else:
		output_obj.set_sentences_using_mp3_path(path_to_file)
	
	# notes = ['The following content is provided under a Creative Commons license',
	# 	'Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free',
	# 	'To make a donation or to view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw',
	# 	'mit',
	# 	'edu',
	# 	"WILLIAM BONVILLIAN: So today, we really kind of talk more about the system, the kind of third direct innovation factor, and then about these indirect factors that are important and significant, but not as powerful, I'd argue, as the direct factors"
	# ]

	notes = output_obj.compute_notes()
	print("notes=", notes[0])

	return render_template('notes.html', notes=notes)
