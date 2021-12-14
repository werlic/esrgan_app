from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=["POST"])
def upload():
    if request.files['image'] != None:
        return "File Upload"
    else:
        return "File not upload!!"