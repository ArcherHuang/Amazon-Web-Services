# *****************************************************************************
# Description: Batch Write Item
# *****************************************************************************
#
# install the required packages
# sudo pip install awscli
# sudo pip install boto3

import boto3

dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('staff')

with table.batch_writer() as batch:  
    batch.put_item(
        Item={
            'account_type': 'standard_user',
            'username': 'stefanb',
            'first_name': 'stefan',
            'last_name': 'bester',
            'age': 30,
            'address': {
                'road': '1 jamesville street',
                'city': 'kroonstad',
                'province': 'free state',
                'country': 'south africa'
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'administrator',
            'username': 'ruanb',
            'first_name': 'ruan',
            'last_name': 'bekker',
            'age': 36,
            'address': {
                'road': '10 peterville street',
                'city': 'cape town',
                'province': 'western cape',
                'country': 'south africa'
            }
        }
    )