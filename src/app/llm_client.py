import os
from typing import List, Dict
from openai import OpenAI


class LLM_Client:
    """
    Component responsible for getting a response from the language model.

    Requires:
      - OPENAI_API_KEY in environment
      - optional MODEL_NAME (defaults to gpt-4o-mini)
    """

    def __init__(self, model: str | None = None):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")

        self.model_name = model or os.getenv("MODEL_NAME", "gpt-4o-mini")
        self.client = OpenAI(api_key=api_key)

    def generate(self, messages: List[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
