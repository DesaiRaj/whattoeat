from dao.ddb import DDBDAO
from domain.response import Ingredient
from domain.response import DishResponse


class DishService():

    def __init__(self):
        self.DAO = DDBDAO()

    def get_ingredient(self, ingredient):
        ingredient_details = self.DAO.get_ingredient(ingredient.id)
        return Ingredient(id=ingredient.id, quantity=ingredient.quantity, name=ingredient_details.name,
                          unit=ingredient_details.unit)

    def get_dish(self, id):
        dish = self.DAO.get_dish(id)
        ingredient_details = []
        for ingredient in dish.ingredients:
            ingredient_detail = self.get_ingredient(ingredient)
            ingredient_details.append(ingredient_detail)

        return DishResponse(id=dish.id,
                            name=dish.name,
                            description=dish.description,
                            detailed_description=dish.detailed_description,
                            images=dish.images,
                            ingredients=ingredient_details,
                            videos=dish.videos)
