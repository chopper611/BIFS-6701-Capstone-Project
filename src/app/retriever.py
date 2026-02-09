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
    
    #This retriever stub will be replaced by the Retrieval Augmented Generation (RAG)
    # K= 4, return most relevant 4 chunks
    def retrieve(self, question: str, k: int = 4) -> List[Chunk]:

    """
    Inputs: 
    question: the student's question
    k: number of chunks to return

    Output:
    A list of Chunk objects representing relevant course material

    Stub behavior:
    Returns example chunks
    """

#Replace these demo chunks with real data from BIFS614
#Higher score = higher relevance 
#Lower score = lower relevance 
#Score is optional, may or may not keep it

demo_chunks = [
    Chunk(text = "Take an input DNA sequence", 
    source = "week 1 lecture.doc"
    score = 0.78
    )
]

#Return only the top-k chunks 
return demo_chunks[:k]


#If a user asks for 0 or negative chunks, return nothing 
if k < 0:
    return[] 

