import unittest
from suggestion_service.suggestion_service import SuggestionService
from zoneinfo import ZoneInfo
from datetime import datetime
from suggestion_service.suggestion_service import SuggestionService
from domain.response import Date
from domain.response import SuggestionResponse


class TestSuggestionServiceSpec(unittest.TestCase):

    def test_get_dish(self):
        suggestions = SuggestionService().get_suggestion()

        dt = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
        date = Date(date=dt.__str__(), day=dt.strftime('%A').__str__(), zone="Asia/Kolkata")
        response = SuggestionResponse(date=date, suggestions=suggestions)
        print(SuggestionResponse.to_json(response))
