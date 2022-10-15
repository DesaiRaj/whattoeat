import boto3
from domain.dish import Dish
from domain.ingredient import Ingredient


class DDBDAO():

    def __init__(self):
        self.ingredient_table = boto3.resource('dynamodb').Table('whattoeat-dev-ingredients')
        self.dishes_table = boto3.resource('dynamodb').Table('whattoeat-dev-dishes')

    def add_ingredient(self, id, name, unit):
        self.ingredient_table.put_item(Item={'id': id, 'name': name, 'unit': unit})

    def get_ingredient(self, id):
        response = self.ingredient_table.get_item(Key={'id': id})
        item = response['Item']
        return Ingredient.from_dict(item)

    def add_dish(self, id, dish_details):
        self.dishes_table.put_item(Item={'id': id, 'dish_details': dish_details})

    def get_dish(self, id):
        response = self.dishes_table.get_item(Key={'id': id})
        dish_exists = True if 'Item' in response else False

        item = response['Item']['dish_details']
        return Dish.from_json(item)



