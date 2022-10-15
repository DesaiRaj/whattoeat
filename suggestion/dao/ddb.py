import boto3
from domain.dish import Dish
from domain.suggestion import Suggestions


class DDBDAO():

    def __init__(self):
        self.dishes_table = boto3.resource('dynamodb').Table('whattoeat-dev-dishes')
        self.suggestions_table = boto3.resource("dynamodb").Table('whattoeat-dev-suggestions')

    def get_dish(self, id):
        response = self.dishes_table.get_item(Key={'id': id})
        dish_exists = True if 'Item' in response else False

        item = response['Item']['dish_details']
        return Dish.from_json(item)

    def set_suggestion(self, day, suggestions, category='default'):
        self.suggestions_table.put_item(Item={'day': day, 'category': category, 'suggestions': suggestions})

    def get_suggestion(self, day, category='default'):
        response = self.suggestions_table.get_item(Key={'day': day, 'category': category})
        suggestion_exists = True if 'Item' in response else False

        item = response['Item']['suggestions']
        return Suggestions.from_json(item)




