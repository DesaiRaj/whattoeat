from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Ingredient:
    id: str
    name: str
    unit: str

