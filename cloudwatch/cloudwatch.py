import boto3
import os
from main import main 

cloudwatch_events = boto3.client('events', 
                                 region_name='us-east-1',
                                 aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                                 aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY_ID'])

main.parameters()


def rule():
    response = cloudwatch_events.put_rule(
        Name='schedule_event',
        RoleArn='arn:aws:iam::916171215187:role/ScheduleAcess',
        ScheduleExpression='cron({} {} {} {} {} {})'.format(main.parameters.minute,
                            main.parameters.hour, main.parameters.day, main.parameters.month, "?", main.parameters.year),
        State='ENABLED'
    )
    print(response['RuleArn'])


    response = cloudwatch_events.put_targets(
        Rule='schedule_event',
        Targets=[
            {
                'Arn': 'arn:aws:lambda:us-east-1:916171215187:function:schedule-job-ec2',
                'Id': 'myCloudWatchEventsTarget',
            }
        ]
    )
    print(response)

    return response