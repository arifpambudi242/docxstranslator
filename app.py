import json, os
from flask import Flask , render_template, Response, request, jsonify, flash
from time import sleep
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        path = os.path.join('./upload', filename).replace('\\', '/')
        f.save(path)
        response = app.response_class(
            response=json.dumps({'success' : True, 'message' : 'File Uploaded!' }),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
	    return render_template('base.html')

if __name__ == '__main__':

	app.run(debug=True)
