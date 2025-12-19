import os
from openai import OpenAI
from dotenv import load_dotenv
from backend.retrieval import retrieve

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_KEY"))

def call_llm(system_prompt, user_prompt): #calls the llm using the system prompt (written by me) and the user prompt.
    response = client.responses.create(model = "gpt-4o-mini", input = [{"role": "system", "content": system_prompt}, {"role": "user", "content" : user_prompt}])
    return response.output_text

def generate_draft(question, notes): #generate the inital draft and call the llm using both the question and the recieved notes.
    system_prompt = ("You are an intro to CS study assistant." " Answer ONLY using the provided notes." " If the notes do not contain the notes, say the following: 'I do not know based on the notes.'")
    user_prompt = f"QUESTION:\n{question}\n\nNOTES:\n{notes}"
    return call_llm(system_prompt, user_prompt)

def validate_answer(question, notes, draft): #takes the question, the notes, and the inital draft and fixes it and improves it
    system_prompt = ("You are validating an answer. Compare the DRAFT to the NOTES." " Fix mistakes, fill gaps, and ensure accuracy." " Return an improved final answer.")
    user_prompt = f"QUESTION:\n{question}\n\nNOTES:\n{notes}\n\nDRAFT ANSWER:\n{draft}"
    return call_llm(system_prompt, user_prompt)

def run_agent(question, debug=False): #runs the agent. 1. retrieves notes 2. creates draft 3. creates final answer.
    results = retrieve(question, k = 3) 
    if not results:
        return "No notes were retrieved."
    retrieved_docs = results["documents"][0]
    notes = "\n\n---\n\n".join(retrieved_docs)
    draft = generate_draft(question, notes)
    final = validate_answer(question, notes, draft)

    return final

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question: ")
        print("\nAnswer:")
        print(run_agent(q))
