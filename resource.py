import process
import boto3
import os

def rule():
    transform = process.Transform()
    param = transform.parameters()

    cloudwatch_events = boto3.client(
        'events', region_name='us-east-1', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY_ID'])

    response = cloudwatch_events.put_rule(
        Name='schedule_event',
        RoleArn='arn:aws:iam::916171215187:role/ScheduleAcess',
        ScheduleExpression='cron({} {} {} {} {} {})'.format(param[0],
                                                            param[1],
                                                            param[2],
                                                            param[3],
                                                            "?",
                                                            param[4]),
        State='ENABLED'
    )
    
    response = cloudwatch_events.put_targets(
        Rule='schedule_event',
        Targets=[
            {
                'Arn': 'arn:aws:lambda:us-east-1:916171215187:function:schedule-job-ec2',
                'Id': 'myCloudWatchEventsTarget',
            }
        ]
    )

    client = boto3.client('lambda', region_name='us-east-1', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY_ID'])

    response = client.create_function(
        FunctionName='schedule-job-ec2',
        Runtime='python3.6',
        Role='arn:aws:iam::916171215187:role/ScheduleAcess',
        Handler='handler.lambda_to_ec2',
        Code={'ZipFile': open('./schedule-handler.zip', 'rb').read()}
    )
    
    print(response)
