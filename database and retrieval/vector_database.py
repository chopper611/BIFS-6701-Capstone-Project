import os
import json
import uuid6
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#initialize variables
collection_name = "BIFS614"
embedding_model = "text-embedding-3-small"
json_file = "chunks.json"
openai_api_key = os.getenv("OPENAI_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

#initialize openai client and qdrant client
openai_client = OpenAI(api_key = openai_api_key)   
qdrant_client = QdrantClient(url = qdrant_url, grpc_port = 6334, prefer_grpc = True, api_key = qdrant_api_key)

#function to generate embeddings
def generate_embeddings(text):
    response = openai_client.embeddings.create(input = text, model = embedding_model)
    return [data.embedding for data in response.data]
    
#function that extracts and processes data from json file, then upserts processed data into qdrant cloud
def add_data_qdrantcloud():
    #load data from json file
    try:
        with open(json_file, 'r') as file:
            chunked_data = json.load(file)

    except FileNotFoundError:
        print("Error: File not found.")
        return
    
    except json.JSONDecodeError:
        print("Error: Could not decode JSON file.")
        return


    #extract text that will be used for embedding
    text = [item.get("text", "") for item in chunked_data]
    if not text:
        print("No text data was found in json file")


    #create embeddings
    embeddings = generate_embeddings(text)
    

    #create qdrant collection if it does not exist
    if not qdrant_client.collection_exists(collection_name = collection_name):
        qdrant_client.create_collection(
            collection_name = collection_name,
            vectors_config = VectorParams(size = 1536, distance = Distance.COSINE),
            )
        print(f"The {collection_name} collection has been created")
    else:
        print(f"The {collection_name} collection already exists")


    #create points to upsert into qdrant
    points = [
        PointStruct(
            id = str(uuid6.uuid7()),
            vector = embeddings,
            payload = item
            )
        for idx, (embeddings, item) in enumerate(zip(embeddings, chunked_data))
        ]
    print("points have been created from file contents")
   
    #upsert points
    qdrant_client.upsert(
        collection_name = collection_name,
        points = points
        )
    print(f"{len(points)} points have been upserted into the collection")

add_data_qdrantcloud()












    
