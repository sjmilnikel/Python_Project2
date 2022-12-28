#Create a Standard SQS Queue using boto3 Python
import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='scm_sqs_lambda')

# You can now access identifiers and attributes
print(queue.url)
