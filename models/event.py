
from dataclasses import dataclass
from typing import Dict

@dataclass
class Event:
    id: int
    type: str
    description: str
    outcomes: Dict[str, str]  # decision → outcome label
