#src/app/retriever.py

from typing import List
from .types import Chunk 

class Retriever: 
    """ 
    Retriever = component that returns relevant course content ("chunks") based on a student's question.

    A STUB: 
    -returns hardcoded chunks so that the application flow can be built/tested now
    -later replaced by embeddings + vector database search (RAG)
    """
    
    def retrieve(self, question: str, k: int = 4) List[Chunk]:
    """
    Inputs: 
    question: the student's question
    k: number of chunks to return

    Output:
    A list of Chunk objects representing relevant course material

    Stub behavior:
    Returns example chunks