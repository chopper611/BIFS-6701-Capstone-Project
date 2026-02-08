# src/app/llm_client.py

from typing import List, Dict

class LLM_Client: 
    """
    LLM_Client = The component responsible for getting a response from the language model
    This is a stub version, which does not call a real model
    Returns a placeholder response to test the application flow 
    """

    #Model_name is a placeholder for now
    def __init__(self, model_name: str = "stub-model"):
        self.model_name = model_name

    #Extract the most recent user message to respond to it
    for msg in reversed(messages): 
        if msg.get("role") == "user":
            user_text = msg.get("content", "")
            break 
    else: 
        user_text = ""

    #Find the system message
    for msg in messages:
        if msg.get("role") == "system":
            system_text = msg.get("content", "")
            break 
    else: 
        system_text = ""

        return(f)