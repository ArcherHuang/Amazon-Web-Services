from __future__ import print_function

import json  
import boto3  
from boto3.dynamodb.conditions import Key, Attr

print('Loading function')


def lambda_handler(event, context):  
    dynamodb = boto3.resource('dynamodb').Table('sensingData')

    response = dynamodb.scan(  
        FilterExpression=Attr('Moisture').gt(int(event['params']['querystring']['moisture']))
    )

    items = response['Items'] 

    return {"Moisture":event['params']['querystring']['moisture'], "items": items}  # Echo back the first key value
