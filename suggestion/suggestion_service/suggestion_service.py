from dao.ddb import DDBDAO
from domain.response import Dish
from domain.response import Suggestion
from zoneinfo import ZoneInfo
from datetime import datetime


class SuggestionService():
    def __init__(self):
        self.DAO = DDBDAO()

    def get_today_id(self):
        print(datetime.now(tz=ZoneInfo('Asia/Kolkata')).day)
        return "1"

    def get_dish(self, id):
        dish_details = self.DAO.get_dish(id)
        return Dish(id=dish_details.id,
                    name=dish_details.name,
                    description=dish_details.description,
                    images=dish_details.images)

    def get_suggestion(self):
        id = self.get_today_id()
        suggestion = self.DAO.get_suggestion(id)
        suggestions = []
        for sg in suggestion.dishes:
            dishes = []
            for dish in sg.dishes:
                dish_detail = self.get_dish(dish.id)
                dishes.append(dish_detail)
            suggestions.append(Suggestion(meal=sg.meal, dishes=dishes))
        return suggestions
