import unittest
from dish_service.dish_service import DishService
from domain.response import DishResponse


class TestDishServiceSpec(unittest.TestCase):

    def test_get_dish(self):
        dish = DishService().get_dish("1")
        print(DishResponse.to_json(dish))
