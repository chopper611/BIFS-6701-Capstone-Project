# src/app/llm_client.py

import os 
from openai import OpenAi 
from typing import List, Dict

class LLM_Client: 
    """
    LLM_Client = The component responsible for getting a response from the language model
    Real OpenAI-backed LLM client. THIS WILL USE TOKENS!!
    The code will expect  - OPENAI_API_KEY in .env
                          - MODEL_NAME in env
    """

    #Model_name is a placeholder for now
    def __init__(self, model: str | None = None, api_key: str | None = None):
        self.model_name = model or os.getenv("Model_Name", "gpt-4o-mini")
        api_key = OpenAi(api_key =api_key or os.getenv("OpenAI_Key"))
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        self.client = OpenAI(api_key=api_key)


 
    def generate(self, messages: List[Dict[str, str]]) -> str:
        resp = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.2,
        )
        return resp.choices[0].message.content.strip()
