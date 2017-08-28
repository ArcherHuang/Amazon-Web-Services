from __future__ import print_function

import json
import boto3

client = boto3.client('iot-data', region_name='us-east-1')

print('Loading function')


def lambda_handler(event, context):
    response = client.publish(
        topic='/alertMessage/Room1',
        qos=1,
        payload=json.dumps({"AlertLevel":"0"})
    )
