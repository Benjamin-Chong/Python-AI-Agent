# Python AI Agent

## Overview
- A beginner-focused Python study assistant that answers questions strictly using my own handwritten Markdown notes (credit to *30 Days of Python*).
- GitHub link: https://github.com/Asabeneh/30-Days-Of-Python
- The goal is to help beginners deepen their understanding of fundamental concepts.
- Answers are grounded in my own notes that have been checked and reviewed.

This project is intentionally scoped to an intro-level Python course and prioritizes correctness, transparency, and system design over a larger scope.

## Motivation
- Currently, many AI tools suffer from hallucination and provide answers without giving their source.
- Many tools guess answers instead of letting the user know that they do not know.

This project explores how retrieval-based grounding (RAG) can help alleviate some of these issues.

## High-Level Architecture
The project architecture is layered and follows this flow:

Frontend → Backend → Retrieval + Prompting → Response

- The frontend only handles UI and UX
- The backend only calls the AI agent method
- The frontend never calls any part of the AI agent

## Backend Design

### Request Flow
1. User submits a question from the frontend
2. The backend receives the request via the FastAPI `/ask` endpoint
3. Relevant notes are retrieved
4. A two-part prompting strategy is applied
5. The answer is returned to the frontend

## Two-Part Prompting
1. The first step answers the question using only the retrieved notes (strict prompting).
2. The second step refines the answer using the notes, the first draft, and a flexible prompt.

This separation helps reduce hallucinations while maintaining readability.

## Failure Handling
The system is designed to fail gracefully and remain transparent.

Example scenarios:
1. If no retrieved notes are similar to the question, the assistant informs the user that the topic is not covered.
2. If there is no response from Part 1, the second part does not run.
3. Out-of-scope questions are answered transparently rather than guessed.

The priority was trust and transparency while still balancing a somewhat complete answer when possible.

## Frontend Overview

### Pages
1. **Home Page**: Details the scope and purpose of the project and explains how to use the assistant.
2. **Study Page**: Keeps a record of the messages between the user and the assistant and provides a space for the user to ask questions.
3. **Credits Page**: Credits the author of *30 Days of Python*, explains the tech stack used, and gives credit to OpenAI.

### UI & Styling
- CSS Flexbox layout
- Calm matcha-themed café color palette
- Noto Sans JP font
- Rounded components and reduced visual noise

### Chat Interface Features
- Scrollable chat history
- Messages appended to the chat history
- Distinct colors for user and assistant messages
- Auto-growing textarea
- Custom scrollbar styling

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI, ChromaDB (to store embeddings)
- **AI approach**: RAG, multi-phase prompting
- **Notes**: Markdown files are used to improve AI performance (Markdown files are lightweight and convey meaning effectively)

## Project Scope & Limitations
- Focused on beginner-level Python questions
- Answers are transparent when information does not come from notes
- No authentication or user persistence
- Not intended to replace courses

## Future Improvements
I created a list of potential features that could be added to the project if development were continued:
- Expand note coverage
- Increase the quality of existing notes
- Add automated tests
- Refine documentation

## Why This Project
This was an exploration project to build a full-stack application paired with AI features.

## Getting Started
1. Clone this repository.

![Clone button](assets/clone.png)

*Click on the `<> Code` button first.*

2. Download all required packages from `requirements.txt`.
3. Open the project in your preferred IDE.
4. Start the frontend and backend servers using the following commands:
   - Backend: `uvicorn backend.main:app --reload`
   - Frontend: `python -m http.server 5500`
   - Open: `http://localhost:5500/frontend/homepage.html`
5. Navigate to the study page using the green button labeled **Start Studying** or use the navigation bar at the top.

![Start Study button](assets/study.png)

6. Enter any beginner Python-related question (allow 5–10 seconds for a response):

![Question Box](assets/question.png)

*The answer will appear in the bottom box.*

7. The question and answer pair will be appended to the chat history on the left.

![Chat History](assets/chathistory.png)

## Tests
I created a few tests focusing on important parts of the program:
- Testing the connection to the API
- Ensuring the agent refuses to answer questions outside of the project scope
- Verifying that grounded questions return acceptable responses

## Running Tests
```bash
pip install -r requirements.txt
python -m pytest
```
### Notes on System Limitations
- This project does not cross-reference information across separate note chunks.
- For example, a question like “What is the difference between a string and an integer?” may be declined if those concepts are defined in separate notes.
- To improve trust and reduce hallucinations, the assistant only answers questions when all required information is present within the retrieved context.
- Some comparison questions work when the relevant concepts are documented together.
- For example, “What is the difference between a for loop and a while loop?” is answerable because both concepts are covered within the same note.