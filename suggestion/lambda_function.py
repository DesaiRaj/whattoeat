import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    print("Hello from suggestion lambda")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from suggestion lambda!')
    }