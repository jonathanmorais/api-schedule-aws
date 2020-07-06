from flask import Flask, request, Response
import boto3
from datetime import datetime
import json
import requests
import dateutil
import cloudwatch
from cloudwatch import rule

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/home', methods=['GET'])
def index():
    return 'Suave'

@app.route('/api/scheduler', methods=['POST'])
def parameters():
	r     = request.get_json()
	time  = r['time']
	image = r['docker_image']
	date  = dateutil.parser.parse(time, ignoretz=True)
	year   = str(date).split("-")[0]
	month  = str(date).split("-")[1]
	day    = str(date).split("-")[2][1]
	hour   = str(date).split(":")[0][11:13]
	minute = str(date).split(":")[1][0:2]
    
	cron   = (minute, hour, day, month, year)

	cloudwatch.rule()

	return '''
		IMAGE: {}
		DATE: {}'''.format(image, date)

# start flask app
app.run(host="0.0.0.0", port=5000)
