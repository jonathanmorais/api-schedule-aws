from flask import Flask, request, Response
import boto3
from datetime import datetime
import json
import requests
import dateutil
from process import parameters
from cloudwatch import rule
from function import create_lambda

def main():
    from flask import request
    parameters()
    rule()
    create_lambda()
    

if __name__ == "__main__":
    main()