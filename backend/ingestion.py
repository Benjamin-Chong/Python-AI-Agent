import os
import glob
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

#Does not run all the time. Loads the knowledge map. Sends to LLM and gets back vectors. Stored into the vector database.
load_dotenv() #loads the OPENAI key.
client = OpenAI(api_key = os.getenv("OPENAI_KEY")) #gets the key and feeds it into OPENAI api to generate embeddings.

chroma_client = chromadb.PersistentClient(path = "vector_store") #creates a storage saved on disk
collection = chroma_client.get_or_create_collection("cs_notes") #creates or gets a collection called cs_notes

def load_markdown_files(path="backend/knowledge_base/*.md"): #creates a list of tuples that each contains the filename and their content within each file.
    files = glob.glob(path) #glob finds all of the files with the matching *.md (wildcard).
    documents = []
    for file in files:
        with open(file, "r", encoding = "utf-8") as f:
            documents.append((file, f.read()))
    return documents
 
def embed_text(text): #send content to OPENAI where you will recieve a vector back (embedding).
    response = client.embeddings.create(model = "text-embedding-3-small", input = text)
    return response.data[0].embedding

def ingest(): #loads all of the files and adds to the collection.
    docs = load_markdown_files()
    for (filename, content) in docs:
        vector = embed_text(content)
        collection.add(ids = [filename], documents = [content], embeddings = [vector])
        print(f'Indexed: {filename}')
    print("Ingestion Complete.")

if __name__ == "__main__":
    ingest()

