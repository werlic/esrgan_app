from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import load_model
import os

UPLOAD_FOLDER = 'upload_file'
SAVE_FOLDER = 'save_file'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=["POST"])
def upload():
    if request.files['image'] != None:
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(f'{app.config["UPLOAD_FOLDER"]}/{filename}')
        return "File Upload"
    else:
        return "File not upload!!"