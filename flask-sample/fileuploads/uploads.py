from flask import Flask, request
from werkzeug import secure_filename

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('/var/www/uploads/' + secure_filename(f.filename))


...