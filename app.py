import psutil
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api")
def api():
    cpu_count = psutil.cpu_count()
    return {
        "username": cpu_count
    }