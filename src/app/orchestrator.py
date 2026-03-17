# src/app/orchestrator.py
# Source: https://www.ibm.com/think/topics/llm-orchestration

from .basic_retrieval import BasicRetriever
from .llm_client import LLM_Client
from .prompts import system_prompt, build_context
from .types import AppResponse, Mode


class Orchestrator:
    """
    The orchestrator connects the full application flow.

    Application flow:
    user question → retriever → context building → LLM → final output
    """

    def __init__(self, retriever: BasicRetriever, llm: LLM_Client):
        # Reference retriever and LLM client
        self.retriever = retriever
        self.llm = llm

    def answer(self, question: str, mode: Mode, k: int = 4) -> AppResponse:
        """
        Routes a user question through retrieval, context building,
        and LLM generation, then returns a structured response.
        """

        # Retrieve relevant course content
        chunks = self.retriever.retrieve(question)

        # Convert chunks into a context block
        context_text = build_context(chunks)

        # Build messages for the LLM
        messages = [
            {"role": "system", "content": system_prompt(mode)},
            {
                "role": "user",
                "content": f"{context_text}\n\nQuestion: {question}"
            }
        ]

        # Ask model to generate a response
        answer_text = self.llm.generate(messages)

        # Return structured response
        return AppResponse(
            answer=answer_text,
            chunks=chunks,
            mode=mode
        )
