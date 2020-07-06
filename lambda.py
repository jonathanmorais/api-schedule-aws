import boto3

client = boto3.client('lambda', 
                      region_name='us-east-1',
                      aws_access_key_id='', 
                      aws_secret_access_key='')

response = client.create_function(
    FunctionName='schedule-job-ec2',
    Runtime='python3.6',
    Role='arn:aws:iam::916171215187:role/ScheduleAcess',
    Handler='handler.lambda_to_ec2',
    Code={'ZipFile': open('./schedule-handler.zip', 'rb').read()}
)
