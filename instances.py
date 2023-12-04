import boto3
import json

ec2 = boto3.resource('ec2')

#create a lmnbda function that lists all instances in account

def lambda_handler(event, context):
    instances = []
    for instance in ec2.instances.all():
        instance_dict = {}
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                instance_dict['Name'] = tag['Value']
        instance_dict['InstanceId'] = instance.id
        instance_dict['State'] = instance.state['Name']

        instances.append(instance_dict)

    return instances

jsondata = lambda_handler(event='', context='')

print(jsondata)