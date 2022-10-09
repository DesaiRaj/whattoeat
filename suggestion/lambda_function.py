import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    print("Hello from zip")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }