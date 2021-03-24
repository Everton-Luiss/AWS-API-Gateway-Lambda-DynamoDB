import json
import boto3
import uuid
from datetime import datetime
import os

# That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like deviceId = event['deviceId']
def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    # Getting the table the table Temperatures object
    tableTemperature = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Getting the current datetime and transforming it to string in the format bellow
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    todo_id = str(uuid.uuid1())
    #deviceId = event['deviceId']
    text = event['text']

    # Putting a try/catch to log to user when some error occurs
    try:

        tableTemperature.put_item(
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
            'body': json.dumps('Error saving the temperature')
        }