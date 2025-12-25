
import openai
from config import OPENAI_API_KEY
from models.character import Character
from models.event import Event
from typing import List

openai.api_key = OPENAI_API_KEY

def generate_narrative(
    character: Character,
    event: Event,
    decision: str,
    outcome: str,
    max_tokens: int = 85
) -> str:
    prompt = (
        f"1-2 sentences, Maze Runner style. "
        f"16-year-old Sam Altman (health {character.health:.0f}) "
        f"chose to {decision} during: {event.description} → {outcome}."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM failed ({e.__class__.__name__}): using fallback text")
        return (
            f"Sam {decision}ed during the {event.type} event. "
            f"Result: {outcome}. Health now {character.health:.0f}."
        )
