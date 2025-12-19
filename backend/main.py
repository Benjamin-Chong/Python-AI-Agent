from fastapi import FastAPI
from pydantic import BaseModel
from backend.agent import run_agent #must be backend.agent because of how the project is ran. it is ran from the root so when looking for imports it needs to be backend (for uvicorn)

app = FastAPI() #creates a fastAPI application instance

class Question(BaseModel): #any request must look like this. input validation. 
    question: str 

@app.post("/ask") #creates an endpoint 
def ask_question(payload: Question): #payload is automatically parsed from json and uses the question class to ensure input validation
    answer = run_agent(payload.question) #calls the entire pipeline
    return {"answer": answer}