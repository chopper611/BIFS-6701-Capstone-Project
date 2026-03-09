import os
from openai import OpenAI
from qdrant_client import QdrantClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
collection_name = os.getenv("QDRANT_COLLECTION_NAME", "BIFS614")
embedding_model = "text-embedding-3-small"
chat_model = "gpt-4o-mini"

openai_api_key = os.getenv("OPENAI_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

# Initialize
openai_client = OpenAI(api_key=openai_api_key)

qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
    prefer_grpc=False,
    check_compatibility=False
)


def generate_embeddings(query: str):
    """Generate an embedding vector for a user query."""
    response = openai_client.embeddings.create(
        input=query,
        model=embedding_model
    )
    return response.data[0].embedding


def context_strength(search_results) -> str:
    """Assess whether the retrieved context is strong enough to answer."""
    if not search_results:
        return "NONE"

    first_payload = search_results[0].payload or {}
    first_text = first_payload.get("text", "")

    if len(first_text.strip()) < 200:
        return "WEAK"

    return "STRONG"


def format_context(search_results) -> str:
    """Format retrieved Qdrant payloads into a cleaner context block."""
    formatted_context = ""

    for i, hit in enumerate(search_results, start=1):
        payload = hit.payload or {}
        source = payload.get("source", "Unknown source")
        chunk_id = payload.get("chunk_id", "Unknown ID")
        text = payload.get("text", "")

        formatted_context += (
            f"Context {i}:\n"
            f"Source: {source}\n"
            f"Chunk ID: {chunk_id}\n"
            f"Text: {text}\n\n"
        )

    return formatted_context.strip()


def answer_question(query: str) -> str:
    """Retrieve context and generate an answer grounded in lecture chunks."""
    query_vector = generate_embeddings(query)

    search_results = qdrant_client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=3
    ).points

    strength = context_strength(search_results)

    if strength == "NONE":
        return (
            "I do not have enough BIFS 614 lecture context to answer this question. "
            "Please specify the topic or week."
        )

    if strength == "WEAK":
        return (
            "The retrieved lecture material may be insufficient to fully answer this question. "
            "Please clarify the topic or ask a more specific question."
        )

    formatted_context = format_context(search_results)

    # Member 3 model instructions 
    system_prompt = (
        "You are a BIFS 614 Tutor and Exam Proctor. "
        "Use ONLY the retrieved BIFS 614 lecture context to answer the user's question. "
        "Do NOT use outside knowledge. "
        "If the answer is not clearly supported by the context, say that you do not have enough "
        "information from the retrieved lecture materials. "
        "Format your response as:\n"
        "1) Answer\n"
        "2) Explanation (bullet points)\n"
        "3) Mini-example\n"
        "4) Quick check question\n"
        "5) Evidence used (source, chunk_id)\n"
        "Be clear, concise, and accurate."
    )

    user_prompt = (
        f"Student Question:\n{query}\n\n"
        f"Retrieved Lecture Context:\n{formatted_context}\n\n"
        "Please answer using only the retrieved lecture context."
    )

    answer = openai_client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    return answer.choices[0].message.content


def main():
    """Run the retrieval tutor in a loop."""
    print("\nBIFS614 Retrieval Tutor")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("What is your question? ").strip()

        if query.lower() in ["exit", "quit"]:
            print("Exiting program.")
            break

        if not query:
            print("Please enter a question.\n")
            continue

        try:
            response = answer_question(query)
            print("\nAnswer:\n")
            print(response)
            print("\n" + "-" * 50 + "\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
