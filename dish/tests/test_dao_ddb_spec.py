import unittest
from dish.dao.ddb import DDBDAO


class TestDAODDBSpec(unittest.TestCase):

    def test_add_ingredient(self):
        DDBDAO().add_ingredient("1", "Oil", "ml")

    def test_get_ingredient(self):
        print(DDBDAO().get_ingredient("1"))

    def test_add_dish(self):
        DDBDAO().add_dish("1", """{"id": "1", "name":"Hello dish","description":"","detailed_description":"","images":[{"name":"hello","link":""}],"ingredients":[{"id":"1","quantity":5}],"videos":[{"name":"hello","link":""}]}""")

    def test_get_dish(self):
        print(DDBDAO().get_dish("1"))