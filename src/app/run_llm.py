# Import functions that construct the pipeline and interpret the mode setting
from .main import build_pipeline, parse_mode

def run_llm(question, mode="study", k=4):
    """
    Runs the LLM pipeline on a given question and returns the result.

    Parameters:
    question (str): The input question from the user
    mode (str): Determines behavior of the model ("study" or "assessment")
    k (int): Number of top relevant chunks to retrieve from the database

    Returns:
    dict: Contains the generated answer and any retrieved source chunks
    """

    # The pipeline is constructed by combining the retriever and LLM client
    orch = build_pipeline()

    # The mode string is converted into the internal Mode type used by the system
    parsed_mode = parse_mode(mode)

    # The orchestrator processes the question using retrieval and LLM generation
    response = orch.answer(question, mode=parsed_mode, k=k)

    # The response is formatted into a dictionary for easier external use
    return {
        "answer": response.answer,                  # The final generated answer
        "chunks": getattr(response, "chunks", [])   # The retrieved supporting chunks
    }