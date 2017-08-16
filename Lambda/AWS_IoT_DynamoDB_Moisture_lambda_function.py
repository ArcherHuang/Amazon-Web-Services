from __future__ import print_function

import json  
import boto3

print('Loading function')

def lambda_handler(event, context):  
    dynamodb = boto3.resource('dynamodb').Table("sensingData")

    print("Moisture value = " + str(event['Moisture']))

    item = {
        'location': 'room1',
        'timeStamp': event['time'],
        'Moisture': event['Moisture']
    }

    # write the todo to the database
    response = dynamodb.put_item(Item=item)

    return event['Moisture']  # Echo back the first key value
