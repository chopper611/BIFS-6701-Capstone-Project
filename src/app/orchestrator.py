# src/app/orchestrator.py
# Source- https://www.ibm.com/think/topics/llm-orchestration


from .types import Mode, AppResponse
from .retriever import Retriever
from.llm_client import LLM_Client
from .prompts import system_prompt, build_context

class orchestrator: 
"""
The orchestrator connects the full application flow
Application flow: user question - retriever - context building - LLM - final output  
"""

#Reference self for the retriever and LLM
def __init__(self, retriever: Retriever, LLM, LLM_Client)
    self.retriever = retriever 
    self.llm = llm


def answer(self, question: str, mode: Mode = "study", k: int = 4) -> AppResponse
    #Retrieve relevant course content
    chunks = self.retriever. retrieve(question, k=k)
    #Convert chunks into a context block
    context_text = build_context(chunks)
    #Build chat style messages for the model LLM 
    messages = [
        {"role": "system", "content": system_prompt(mode)}
        {"role": "user", "content" f"{context_text"}\n\nQuestion: {question}"}
    ]
    #Asks model to create a resonse 
    answer_text = self.llm.generate(messages)
    #Return a structured response 
    return AppResponse(answer = answer_text, chunks = chunks, mode = mode)