import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    print("Hello from dish lambda")
    dish_id = event['pathParameters']['id']
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from {dish_id} dish lambda!')
    }