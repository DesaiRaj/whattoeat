import unittest
from domain.dish import Dish


class TestDomainSpec(unittest.TestCase):

    def test_json_to_dataclass(self):
        json_string = """{"id": "1", "name":"Hello dish","description":"","detailed_description":"","images":[{"name":"hello","link":""}],"ingredients":[{"id":"","quantity":5}],"videos":[{"name":"hello","link":""}]}"""
        data = Dish.from_json(json_string)
        self.assertEqual(data.name, 'Hello dish')