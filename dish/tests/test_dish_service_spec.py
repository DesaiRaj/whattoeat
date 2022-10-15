import unittest
from dish.dish_service.dish_service import DishService
from dish.domain.response import DishResponse


class TestDishServiceSpec(unittest.TestCase):

    def test_get_dish(self):
        dish = DishService().get_dish("1")
        print(DishResponse.to_json(dish))
