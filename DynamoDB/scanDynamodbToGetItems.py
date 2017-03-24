# *****************************************************************************
# Description: can scan the table based on attributes of the items
# *****************************************************************************
#
# install the required packages
# sudo pip install awscli
# sudo pip install boto3
#
# aws configure

import boto3  
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(  
    'dynamodb'#,
    #aws_access_key_id = '',
    #aws_secret_access_key = '',
    #region_name = ''
)  

table = dynamodb.Table('test')

response = table.scan(  
    FilterExpression=Attr('temperature').gt(25) & Attr('timeStamp').eq('temperatureHumidity')
)

items = response['Items']  
#print(items) 

print "Length items: " + str(len(items))

for x in range(len(items)): 
    print "humidity: " + str(items[x]['humidity']) + "\t" + "temperature: " + str(items[x]['temperature'])