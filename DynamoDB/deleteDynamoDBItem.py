# *****************************************************************************
# Description: Updating Items
# *****************************************************************************
#
# install the required packages
# sudo pip install awscli
# sudo pip install boto3
#
# aws configure

import boto3

dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('test')

table.delete_item(  
    Key={
        'topic': 'Room1',
        'timeStamp': '20170320115007'
    }
)