
from models.character import Character
from models.event import Event
from simulation.narrative_generation import generate_narrative
from typing import List
import random

class MazeSimulation:
    def __init__(self, character: Character, events: List[Event]):
        self.character = character
        self.events = events
        self.day = 0
        self.history: List[dict] = []

    def run_day(self) -> bool:
        if self.day >= len(self.events) or self.character.health <= 0:
            print("\n" + "═" * 60)
            print("  SIMULATION COMPLETE  ".center(60, "═"))
            print("═" * 60)
            return False

        event = self.events[self.day]
        print(f"\nDay {self.day + 1:2d}  |  {event.description}")

        decision = self.character.make_decision(event.type)
        outcome = event.outcomes.get(decision, "neutral")

        print(f"   → Decision: {decision}")
        print(f"   → Outcome:  {outcome}")

        self.character.apply_outcome(outcome, event.type)

        narrative = generate_narrative(self.character, event, decision, outcome)
        print(f"\n   {narrative}")

        print(f"   Health: {self.character.health:3.0f}")
        print(f"   Relationships: {', '.join(f'{k}:{v:.2f}' for k,v in self.character.relationships.items())}")

        self.history.append({
            "day": self.day + 1,
            "event": event.description,
            "decision": decision,
            "outcome": outcome,
            "health": self.character.health,
            "relationships": self.character.relationships.copy()
        })

        self.day += 1
        return True

    def run(self):
        print("\n" + "═" * 60)
        print(f"  MAZE RUNNER SIM MVP  -  {self.character.name} (age {self.character.age})")
        print("═" * 60)
        print(f"OCEAN: {self.character.ocean}")
        print("═" * 60)

        while self.run_day():
            pass

        self.print_summary()

    def print_summary(self):
        if not self.history:
            print("No events occurred.")
            return

        print("\n" + "═" * 60)
        print(" SUMMARY TABLE ".center(60, "═"))
        print("Day | Event (short)              | Dec    | Out    | Health | Relations")
        print("-" * 60)

        for h in self.history:
            event_short = h["event"][:26] + "..." if len(h["event"]) > 26 else h["event"]
            rels = ", ".join(f"{k[0]}:{v:.1f}" for k,v in h["relationships"].items())
            print(
                f"{h['day']:3} | {event_short:<26} | {h['decision']:<6} | "
                f"{h['outcome']:<6} | {h['health']:5.0f} | {rels}"
            )
