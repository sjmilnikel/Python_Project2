# how to create or launch EC2 instance using boto3
"""
import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-0b0dcb5067f052a63',    #enter AMI
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3)
 """   
# How to stop all running EC2 instances using boto3 Python
import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]
li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
ec2_client.stop_instances(InstanceIds=li)
li.append(instance_id)