import boto3
import os
import datetime

# print('Loading function')

def lambda_handler(event, context):
    instance_start()
def instance_start():
        ec2 = boto3.client('ec2', region_name='us-east-2')
        desc = ec2.describe_instances(Filters=[{'Name': 'tag:project', "Values": ['Auto']}])

        targets = []
        for reservation in desc['Reservations']:
            for instance in reservation['Instances']:
                if 'Tags' in instance:
                  for tag in instance['Tags']:
                        if tag['Key'] == 'project' and tag['Value'] == 'Auto':
                           targets.append(instance['InstanceId'])
        print(targets)
        tages = []
        for reservation in desc['Reservations']:
            for instance in reservation['Instances']:
                if 'Tags' in instance:
                  for tag in instance['Tags']:
                    if tag['Key'] == 'project' and tag['Value'] == 'Auto':
                        targets.append(instance['InstanceId'])
                    for i in targets:
                           if tag['Key'] == 'Name':
                                tages.append(tag['Value'])
        tagesremove = list(set(tages))
        print(tagesremove)

        status = desc['Reservations'][0]['Instances'][0]['State']['Name']
        print(status)

        if status == "running":
            message = "instance is already running. nothing to do"
        elif status == "stopped":
            ec2.start_instances(InstanceIds=targets)
            message = "instance start"
        else:
            message = "instance is not stopped. can not start instance"

        sns_publish(message)
def sns_publish(message):
    client = boto3.client('sns')
    response = client.publish(
        TopicArn='arn:aws:sns:ap-northeast-1:youracountnumber:sendmail',
        Message=message,
        Subject='['+os.environ['instanceid']+']:startup_instance'
    )
