import os
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

#converts the user question into a vector using embed_text and then searches the vector database for similar nodes. then returns the matched notes.
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

chroma_client = chromadb.PersistentClient(path = "vector_store")
collection = chroma_client.get_or_create_collection("cs_notes")

def embed_text(text):
    response = client.embeddings.create(model = "text-embedding-3-small", input = text)
    return response.data[0].embedding

def retrieve(query, k = 2): #takes the query from the user and returns the amount of results. k depends on how big the knowledge-map. bigger map, bigger n.
    query_vector = embed_text(query) #calls the embed function to get the vectors from the query (user).
    results = collection.query(query_embeddings = [query_vector], n_results = k)
    return results #returns the embedding of the user question and return the results that are most similar.