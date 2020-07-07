import boto3    
import os

ec2 = boto3.client('ec2', region_name='us-east-1',
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY_ID'])

def lambda_to_ec2(event, context):
    init_script = """#!/bin/bash
sudo apt-get update -y
sudo sudo apt-get install docker.io -y
"""

    print ('Running script:')
    print (init_script)

    resp = ec2.run_instances(
        ImageId='ami-0ac80df6eff0e70b5',
        InstanceType='t2.micro',
        MinCount=1, # required by boto, even though it's kinda obvious.
        MaxCount=1,
        KeyName='developer',
        SecurityGroupIds=['sg-0aa23e462e64e2e39'],
        UserData=init_script # file to run on instance init.
    )

    for instance in resp['Instances']:
        print(instance['InstanceId'])
