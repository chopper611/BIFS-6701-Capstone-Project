import os
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#initialize variables
collection_name = "BIFS614"
embedding_model = "text-embedding-3-small"
openai_api_key = os.getenv("OPENAI_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

#initialize openai client and qdrant client
openai_client = OpenAI(api_key = openai_api_key)   
qdrant_client = QdrantClient(url = qdrant_url, grpc_port = 6334, prefer_grpc = True, api_key = qdrant_api_key)

#function to generate embeddings
def generate_embeddings(query):
    response = openai_client.embeddings.create(input = query, model = embedding_model)
    return response.data[0].embedding

#example question
query = input("What is your question? ")

#create embedding from user query
query_vector = generate_embeddings(query)

#perform similarity search (can also add in filering condition if needed)
search_results = qdrant_client.query_points(
    collection_name = collection_name,
    query = query_vector,
    query_filter = None,
    limit = 1
    ).points

#retrieve relevant context
context = [hit.payload for hit in search_results]

#customize prompt
prompt = f"use the following context to answer: {context}"

#use an openai chatgpt model to obtain answer
answer = openai_client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": query}
        ],
        temperature = 0
    )

#print chatgpt answer
print(answer.choices[0].message.content)





