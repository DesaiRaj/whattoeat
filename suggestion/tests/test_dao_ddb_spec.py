import unittest
from dao.ddb import DDBDAO


class TestDAODDBSpec(unittest.TestCase):

    def test_get_dish(self):
        print(DDBDAO().get_dish("1"))

    def test_set_suggestion(self):
        print(DDBDAO().set_suggestion("1", """{"day": "1", "dishes":[{"meal":"BREAKFAST","dishes":[{"id":"1"}]},{"meal":"LUNCH","dishes":[{"id":"1"}]},{"meal":"DINNER","dishes":[{"id":"1"}]}]}"""))

    def test_get_suggestion(self):
        print(DDBDAO().get_suggestion("1"))
