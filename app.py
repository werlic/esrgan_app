from flask import Flask
from flask import request
from flask import render_template
import load_model

UPLOAD_FOLDER = '/upload_file'
SAVE_FOLDER = '/save_file'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=["POST"])
def upload():
    if request.files['image'] != None:
        file = request.files
        return "File Upload"
    else:
        return "File not upload!!"