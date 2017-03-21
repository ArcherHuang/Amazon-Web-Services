import boto3  
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(  
    'dynamodb',
    aws_access_key_id = '',
    aws_secret_access_key = '',
    region_name = 'us-east-1'
)  

table = dynamodb.Table('test')

response = table.get_item(  
   Key={
        'topic': 'Room1',
        'timeStamp': 'temperatureHumidity'
    }
)

item = response['Item']  
name = item['temperature']

print(item)  
print("Hello, {}" .format(name)) 