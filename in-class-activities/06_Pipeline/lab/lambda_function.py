import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    if 'Records' in event:
        record = json.loads(event['Records'][0]['body'])
    else:
        record = event

    if '#uchicago' in record['tweet']:
        table = dynamodb.Table('twitter')
        table.put_item(
           Item={
                'uid': record['datetime'] + '_' + record['username'],
                'username': record['username'],
                'tweet': record['tweet']
            }
        )

    return {'StatusCode': 200}