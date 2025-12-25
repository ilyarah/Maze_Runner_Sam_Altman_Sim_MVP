
import random
from dataclasses import dataclass
from typing import Dict

@dataclass
class Character:
    name: str
    age: int
    ocean: Dict[str, float]
    health: float = 100.0
    relationships: Dict[str, float] = None

    def __post_init__(self):
        if self.relationships is None:
            self.relationships = {
                "Newt": 0.5,
                "Thomas": 0.3,
                "Chuck": 0.4
            }

    def make_decision(self, event_type: str) -> str:
        try:
            if event_type == "danger":
                return "explore" if random.random() < self.ocean["O"] else "hide"
            if event_type == "social":
                return "befriend" if random.random() < self.ocean["A"] else "observe"
            if event_type in ("exploration", "maze"):
                return "explore" if random.random() < self.ocean["E"] else "cautious"
            return "default"
        except KeyError as e:
            print(f"Warning: Missing OCEAN trait {e}. Using default decision.")
            return "default"

    def apply_outcome(self, outcome: str, event_type: str):
        delta_health = 0
        if outcome == "positive":
            delta_health = +8
        elif outcome == "negative":
            delta_health = -12

        self.health = max(0.0, min(100.0, self.health + delta_health))

        # Social events affect relationships
        if event_type == "social":
            delta_rel = 0.12 if outcome == "positive" else -0.10
            for name in self.relationships:
                self.relationships[name] = max(0.0, min(1.0, self.relationships[name] + delta_rel))
