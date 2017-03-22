from __future__ import print_function

import logging
import json
import boto3

print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#dynamodb = boto3.resource('dynamodb')
#table = dynamodb.Table('test')

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb').Table("test")
    #print("Received event: " + json.dumps(event, indent=2))
    logger.info('got event{}'.format(event))
    print("temperature value = " + event['temperature'])
    print("humidity value = " + event['humidity'])
    
    item = {
        'topic': event['location'],
        'temperature': event['temperature'],
        'humidity': event['humidity'],
        'timeStamp': event['time']
    }

    # write the todo to the database
    response = dynamodb.put_item(Item=item)
    
    return event['humidity']  # Echo back the first key value
    #raise Exception('Something went wrong')
