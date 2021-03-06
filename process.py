import datetime
import requests
from flask import Flask, request, Response
import dateutil
import boto3
import os
from resource import rule

# Initialize the Flask application
app = Flask(__name__)


# start flask app
app.run(host="0.0.0.0", port=5000)
@app.route('/api/scheduler', methods=['POST'])

class Transform(object):
    def __init__(self):
        self.parameters = self.parameters()

    def parameters(self):
	    r      = request.get_json()
	    time   = r['time']
	    image  = r['docker_image']
	    date   = dateutil.parser.parse(time, ignoretz=True)
	    year   = str(date).split("-")[0]
	    month  = str(date).split("-")[1]
	    day    = str(date).split("-")[2][1]
	    hour   = str(date).split(":")[0][11:13]
	    minute = str(date).split(":")[1][0:2]

	    cron   = [minute, hour, day, month, year]

	    return cron

rule()