# Python AI Agent

## Overview
- A beginner focused Python study asssistnat that answers questions strictly using my own handwritten markdown notes (credit to 30 Days of Python).
- Github Link: https://github.com/Asabeneh/30-Days-Of-Python
- The goal is to help beginners deepen their understanding of fundamental concepts.
- Answers are grounded in my own notes that have been checked through.
This project is intentionaly scoped to an intro-level Python course and prioritizes correctness, transparency, and system design over a larger scope.

## Motivation
- Currently, many AI tools suffer from hallucination, provide answers without giving their source.
- Guess answers, as opposed to letting the user know that they do not know.
This project explores how retrieval-based grounding (RAG) can help alleviate some of these issues.

# High Level Architecture
The project achitecture is a layered architecture and goes as follows: Frontend -> Backend -> Retrieval + Prompting -> Response
- Frontend only handles the UI and UX
- Backend calls ONLY calls the AI Agent method
- Frontend NEVER calls any part of the AI agent

# Backend Design
Request Flow
1. User submits a question from the frontend
2. Backend receives a request via FastAPI /ask endpoint
3. The relevant notes are retrieved
4. Two-part prompting strategy is applied.
5. Answer is returned to the frontend

## Two-part Prompting
1. The first step is to answer the question using ONLY then retrieved notes (strict prompting).
2. The second step is to refine the answer using the notes, the first draft, and the second prompt (flexible).
This separation helps reduce hallucinations while maintaining readabilty.

## Failure Handling
- My system is designed to fail gracefully and is extremely transparent.
Example:
1. If there are notes retrieved are not similar to the question, the assisant informs the user that the topic is not covered.
2. If there is no response from Part 1, the second part will nto run.
3. Out of scope questions are answered transparently rather than guessed.
My priority was trust and transparency, while balancing a somewhat complete answer.

# Frontend Overview
## Pages
1. Home Page: details the scope and the purpose of this project. It briefly explains to the user how to use the assistant.
2. Study Page: keeps a record of the messages between the user and the assistant and has a space for the user to ask questions.
3. Credits Page: credits the author of the 30 days of Python, explains the stack used, gives credit to OpenAI.

## UI & Styling
- CSS Flexbox layout
- Calm matcha themed cafe color pallete
- Noto Sans JP font
- Rounded components and reduced visual noise

## Chat Interface Features
- Scrollable chat history
- Messages appended to the chat history
- Distinct colors for user and assistant messages
- Auto growing textarea
- Custom Scrollbar styling

# Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI, ChromaDB (to store embeddings)
- AI approach: RAG, multi-phase prompting
- Notes: used .md files to improve AI performance (md files are lightweight and conveys meaning better)

# Project Scope & Limitations
- Focused on beginner level questions.
- Answers are transparent when answers do not come from notes.
- No authentication or user persistence
- Not intended to replace courses

# Future Improvements
- Expand note coverage
- Increase quality of existing notes
- Add automated tests
- Refine documentation

## Why This Project
This was an exploration project to explore the full stack paired with AI features.

### Getting Started
(Continued)

### Tests
(Continued)