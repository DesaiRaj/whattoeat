from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Date:
    date: str
    day: str
    zone: str


@dataclass_json
@dataclass
class Link:
    name: str
    link: str


@dataclass_json
@dataclass
class Dish:
    id: str
    name: str
    description: str
    images: List[Link]


@dataclass_json
@dataclass
class Suggestion:
    meal: str
    dishes: List[Dish]


@dataclass_json
@dataclass
class Suggestions:
    suggestions: List[Suggestion]


@dataclass_json
@dataclass
class SuggestionResponse:
    date: Date
    suggestions: Suggestions
