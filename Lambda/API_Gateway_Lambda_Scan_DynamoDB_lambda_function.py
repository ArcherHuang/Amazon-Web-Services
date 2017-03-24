from __future__ import print_function

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

print('Loading function')


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb').Table('test')
    
    response = dynamodb.scan(  
        FilterExpression=Attr('temperature').gt(int(event['params']['querystring']['temperature']))
    )

    items = response['Items'] 

    return {"temperature":event['params']['querystring']['temperature'], "items": items}  # Echo back the first key value

