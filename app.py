import psutil
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api")
def api():

    # define dictionary for saving metrics of server
    metrics = {}

    # get the number of cpus
    metrics.update(cpu_count=psutil.cpu_count())

    # get the system wide cpu utilization
    metrics.update(cpu_utilization=psutil.cpu_percent())

    # get the utilization for each cpu
    metrics.update(cpu_utilization_per_cpu=psutil.cpu_percent(percpu=True))

    # get the cpu frequences
    psutil.cpu_freq(percpu=False)

    # get the memory of the server
    metrics.update(memory=psutil.virtual_memory())

    return {
        "metrics": metrics
    }