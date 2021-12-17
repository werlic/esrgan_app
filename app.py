from flask import Flask, request, url_for, render_template, redirect
from flask.helpers import flash, send_from_directory
from werkzeug.utils import secure_filename
import load_model as model
import os

UPLOAD_FOLDER = 'upload_file'
SAVE_FOLDER = 'save_file'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SAVE_FOLDER'] = SAVE_FOLDER

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=["POST"])
def upload():
    if request.files['image'] != None:
        file = request.files['image']
        filename = secure_filename(file.filename)
        file_path = f'{app.config["UPLOAD_FOLDER"]}/{filename}'
        file.save(file_path)
        print('File Uploaded')
        model.run_model(file_path, app.config["SAVE_FOLDER"] + '/' + filename)
        return redirect(url_for('result', filename=filename))
    else:
        flash('File not uploaded!! Please try again.', 'error')
        return url_for('home')

@app.route('/upload-file/<filename>', methods=['GET'])
def uploaded(filename):
    # #file = open(f'{app.config["UPLOAD_FOLDER"]}/{filename}', 'r')
    # file = f'{app.config["UPLOAD_FOLDER"]}/{filename}'
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/result/<filename>", methods=['GET'])
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/result-file/<filename>', methods=['GET'])
def result_file(filename):
    return send_from_directory(app.config["SAVE_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))