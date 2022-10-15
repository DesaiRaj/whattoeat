from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Dish:
    id: str


@dataclass_json
@dataclass
class Suggestion:
    meal: str
    dishes: List[Dish]


@dataclass_json
@dataclass
class Suggestions:
    day: str
    dishes: List[Suggestion]

