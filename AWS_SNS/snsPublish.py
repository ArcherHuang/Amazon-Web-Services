# export AWS_ACCESS_KEY_ID=
# export AWS_SECRET_ACCESS_KEY=
# export -p

import json
import boto3

sns = boto3.resource('sns', 'us-east-1')
topic = sns.Topic('arn:aws:sns:us-east-1:493439025901:alertMessage')
response = topic.publish(
    Subject="test",
    Message="This is a message.",
)