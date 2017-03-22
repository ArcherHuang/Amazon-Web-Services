from __future__ import print_function

import json
import boto3
import logging

print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    
    #operation = event['context']['http-method']
    
    dynamo = boto3.resource('dynamodb').Table('test')
    response = dynamo.get_item(  
        Key={
            'topic': 'Room1',
            'timeStamp': 'temperatureHumidity'
        }
    )
    item = response['Item']  
    name = item['temperature']
    logger.info('got event{}'.format(item))
    return name
