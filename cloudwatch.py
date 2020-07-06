import boto3
from main import parameters

cloudwatch_events = boto3.client('events', 
                                 region_name='us-east-1',
                                 aws_access_key_id='',
                                 aws_secret_access_key='')


parameters()

def rule():
    response = cloudwatch_events.put_rule(
        Name='schedule_event',
        RoleArn='arn:aws:iam::916171215187:role/ScheduleAcess',
        ScheduleExpression='cron({} {} {} {} {} {})'.format(parameters.minute,
                            parameters.hour, parameters.day, parameters.month, "?", parameters.year),
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