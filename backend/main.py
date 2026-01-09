from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.agent import run_agent #must be backend.agent because of how the project is ran. it is ran from the root so when looking for imports it needs to be backend (for uvicorn)
import time

#use this to run uvicorn backend.main:app --reload

app = FastAPI() #creates a fastAPI application instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://python-ai-agent-git-main-benjamin-chongs-projects-8f4e574f.vercel.app"],  # frontend origin     
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel): #any request must look like this. input validation. 
    question: str 

@app.post("/ask") #creates an endpoint
def ask_question(payload: Question): #payload is automatically parsed from json and uses the question class to ensure input validation
    start = time.perf_counter()
    answer = run_agent(payload.question) #calls the entire pipeline
    elapsed = time.perf_counter() - start
    print(f"Retrieval time: {elapsed:.3f}s")
    return {"answer": answer}