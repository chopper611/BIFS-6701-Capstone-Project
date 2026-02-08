#src/app/types.py
#Source - https://docs.langchain.com/oss/python/langchain/rag
#Source - https://dev.to/zachary62/retrieval-augmented-generation-rag-from-scratch-tutorial-for-dummies-508a

from dataclasses import dataclass
from typing import Optional, List, Literal

Mode = Literal["study", "assessment"]

@dataclass 
Class Chunk: 
    text:str
    source: str
    score: optional[float] = None

@dataclass 
Class Appresponse:
    answer: str
    chunks: List[Chunk]
    mode: Mode


