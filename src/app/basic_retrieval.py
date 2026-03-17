import os


from openai import OpenAI
from qdrant_client import QdrantClient
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv(override=True)

#initialize variables
collection_name = "BIFS614"
embedding_model = "text-embedding-3-small"
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")



class BasicRetriever:
    def __init__(self, k: int = 4):
        self.k = k
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            grpc_port=6334,
            prefer_grpc=True,
            api_key=os.getenv("QDRANT_API_KEY")
        )

    def retrieve(self, query: str):
        query_vector = generate_embeddings(query)

        results = self.qdrant_client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=self.k
        ).points

        return [
            {
                "text": hit.payload,
                "score": hit.score,
                "source": hit.payload.get("source")
                if isinstance(hit.payload, dict)
                else None,
            }
            for hit in results
        ]


        qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            grpc_port=6334,
            prefer_grpc=True,
            api_key=os.getenv("QDRANT_API_KEY")
        )

        results = qdrant_client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=self.k
        ).points

        return [
            {
                "text": hit.payload,
                "score": hit.score,
                "source": hit.payload.get("source")
                if isinstance(hit.payload, dict)
                else None,
            }
            for hit in results
        ]


#initialize openai client
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)


#function to generate embeddings
def generate_embeddings(query):
    openai_client = get_openai_client()
    response = openai_client.embeddings.create(
        input=query,
        model=embedding_model
    )
    return response.data[0].embedding


if __name__ == "__main__":
    openai_client = get_openai_client()
    qdrant_client = QdrantClient(
        url=qdrant_url,
        grpc_port=6334,
        prefer_grpc=True,
        api_key=qdrant_api_key
    )

    #get user input
    query = input("What is your question? ")

    #create embedding from user query
    query_vector = generate_embeddings(query)

    # perform similarity search
    search_results = qdrant_client.query_points(
        collection_name=collection_name,
        query=query_vector,
        query_filter=None,
        limit=1
    ).points

    #retrieve relevant context
    context = [hit.payload for hit in search_results]

    #customize prompt
    prompt = f"use the following context to answer: {context}"

    #get answer
    answer = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ],
        temperature=0
    )

    print(answer.choices[0].message.content)

