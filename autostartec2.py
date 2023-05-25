import boto3
region = 'DefineYourRegionHere'
instances = ['INSTANCEID-1','INSTANCEID-2','INSTANCEID-3']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
