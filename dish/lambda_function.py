from dish_service.dish_service import DishService
from domain.response import DishResponse


def lambda_handler(event, context):
    dish_id = event['pathParameters']['id']
    print(f"Getting dish details for {dish_id}")
    dish = DishService().get_dish(dish_id)
    return {
        'statusCode': 200,
        'body': DishResponse.to_json(dish)
    }