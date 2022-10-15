import json
import boto3
from zoneinfo import ZoneInfo
from datetime import datetime
from suggestion_service.suggestion_service import SuggestionService
from domain.response import Date
from domain.response import SuggestionResponse


def lambda_handler(event, context):
    suggestions = SuggestionService().get_suggestion()

    dt = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
    date = Date(date=dt.__str__(), day=dt.strftime('%A').__str__(), zone="Asia/Kolkata")
    response = SuggestionResponse(date=date, suggestions=suggestions)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': SuggestionResponse.to_json(response)
    }