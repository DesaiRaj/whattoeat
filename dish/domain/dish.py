from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Ingredient:
    id: str
    quantity: float


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
    detailed_description: str
    images: List[Link]
    ingredients: List[Ingredient]
    videos: List[Link]

