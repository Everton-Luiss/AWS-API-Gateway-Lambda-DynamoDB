import json
import boto3
import uuid
from datetime import datetime
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    todo_id = str(uuid.uuid1())
    text = event['text']

     if 'text' not in event:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item. Insert a text key.'})}

    if not event['text']:
        logging.error('Validation Failed - text was empty. %s', event)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'})}
    else:
        try:

            table.put_item(
                Item={
                    'eventDateTime': eventDateTime,
                    'todo_id': todo_id,
                    'text': text
                }
            )

            return {
                'statusCode': 200,
                'body': json.dumps('Succesfully inserted temperature!')
            }
        except:
            print('Closing lambda function')
            return {
                'statusCode': 400,
                'body': json.dumps('Error saving text')
            }