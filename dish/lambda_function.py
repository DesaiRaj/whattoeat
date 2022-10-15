from dish_service.dish_service import DishService
from domain.response import DishResponse
from domain.response import Date
from zoneinfo import ZoneInfo
from datetime import datetime


def lambda_handler(event, context):
    dish_id = event['pathParameters']['id']
    print(f"Getting dish details for {dish_id}")
    dish = DishService().get_dish(dish_id)

    dt = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
    date = Date(date=dt.__str__(), day=dt.strftime('%A').__str__(), zone="Asia/Kolkata")
    response = DishResponse(date=date, dish=dish)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': DishResponse.to_json(response)
    }
