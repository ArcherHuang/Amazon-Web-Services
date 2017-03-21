import boto3
 
dynamodb_client = boto3.resource(  
    'dynamodb',
    aws_access_key_id = '',
    aws_secret_access_key = '',
    region_name = 'us-east-1'
)

table = dynamodb_client.Table('staff')
 
table.put_item(  
    Item={
        'username': 'ruanb',
        'first_name': 'ruan',
        'last_name': 'bekker',
        'age': 30,
        'account_type': 'administrator',
    }
)
