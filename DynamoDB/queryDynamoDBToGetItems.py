# *****************************************************************************
# Description: Query you can query on the Hash key, but not on the Range key
# *****************************************************************************
#
# install the required packages
# sudo pip install awscli
# sudo pip install boto3


import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(  
    'dynamodb'#,
    #aws_access_key_id = '',
    #aws_secret_access_key = '',
    #region_name = ''
)

table = dynamodb.Table('staff')

response = table.query(  
    KeyConditionExpression=Key('username').eq('ruanb')
)

items = response['Items']  
print(items)  