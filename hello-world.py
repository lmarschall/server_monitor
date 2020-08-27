import psutil
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/cpu_count")
def me_api():
    cpu_count = psutil.cpu_count()
    return {
        "username": cpu_count
    }