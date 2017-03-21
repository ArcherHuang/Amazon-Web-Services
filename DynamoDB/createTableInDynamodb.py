import boto3

dynamodb = boto3.resource(  
    'dynamodb',
    aws_access_key_id = '',
    aws_secret_access_key = '',
    region_name = 'us-east-1'
)

table = dynamodb.create_table(  
    TableName='staff',
    KeySchema=[
        {
            'AttributeName': 'username', 
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name', 
            'KeyType': 'RANGE'
        }
    ], 
    AttributeDefinitions=[
        {
            'AttributeName': 'username', 
            'AttributeType': 'S'
        }, 
        {
            'AttributeName': 'last_name', 
            'AttributeType': 'S'
        }, 
    ], 
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)

print(table.item_count)  
