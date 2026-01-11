# Python AI Agent (Deployed)

A deployed full-stack **Python AI study assistant** that answers questions *grounded in user-provided notes* using a retrieval-augmented generation (RAG) pipeline. The system is designed to prevent hallucinations by restricting responses strictly to relevant retrieved content.

---

## Live Demo

- Frontend **(Vercel)**: https://python-ai-agent-snowy.vercel.app

---

## 🚀 Overview

Large language models can generate convincing but incorrect answers.
**Python AI Agent** addresses this problem by combining vector search with controlled prompting so that responses are generated **only** from existing notes.

The application is deployed with a **FastAPI backend** and a **static frontend**, emphasizing correctness, transparency, and backend system design.

---

## 🧠 Features

- Retrieval-augmented generation (RAG) using ChromaDB vector search
- Context-aware responses grounded in user notes
- Pytest-based unit tests for APIs and retrieval logic
- Backend performance optimizations through persisted embeddings
- Deployed backend and frontend with environment-based configuration
- Transparent fallback behavior when no relevant content is found

---

## ⚙️ Tech Stack

- **Backend:** Python, FastAPI
- **Vector Store:** ChromaDB
- **Frontend:** HTML, CSS, JavaScript
- **AI Pattern:** Retrieval-Augmented Generation (RAG)
- **Testing:** Pytest
- **Deployment:** Railway (backend), Vercel (frontend)

---

## 🗺️ High-Level Architecture

Frontend → FastAPI Backend → Vector Search (ChromaDB) → Prompt Logic → Response

1. User submits a question
2. Backend retrieves the most relevant note embeddings
3. Prompt is constructed using retrieved context
4. The model generates a grounded response
5. Response is returned to the frontend

---

## 📥 Quick Start (Local)

### 1) Clone the Repository

git clone https://github.com/Benjamin-Chong/Python-AI-Agent.git  
cd Python-AI-Agent

### 2) Install Dependencies

pip install -r requirements.txt

### 3) Run the Backend

uvicorn backend.main:app --reload

### 4) Run the Frontend

python -m http.server 5500

Open your browser at:  
http://localhost:5500/frontend/index.html

---

## 💡 Usage

1. Open the home page
2. Click **Start Studying**
3. Ask a question in the chat interface
4. The assistant responds using only relevant notes

If no relevant content is found, the system responds transparently instead of hallucinating.

---

## 🧪 Running Tests

pip install -r requirements.txt  
python -m pytest

Tests validate:
- REST endpoint behavior
- Retrieval and vector search logic
- Correct handling of edge cases

---

## 📌 Deployment

- Backend deployed on **Railway**
- Frontend deployed on **Vercel**
- Environment-based secrets and configuration used for production
- CORS and production startup commands configured for deployment

---

## 📚 Motivation

This project explores how retrieval-augmented generation can improve trustworthiness in AI systems by grounding responses in real, user-provided data rather than relying solely on generative behavior.

---

## ⚠️ Limitations

- No user authentication or persistence
- Answer quality depends on the quality and scope of notes
- Limited to single-user local usage in its current form
- The agent may refuse to answer certain questions if the relevant concept is not retrieved, even when the information exists elsewhere in the notes. This is an intentional design choice to prioritize grounded responses and avoid hallucination. A future improvement would involve splitting notes into smaller, concept-level chunks to improve retrieval recall without weakening trust guarantees.

---

## 🛠️ Future Improvements

- User authentication and note persistence
- Expanded note indexing and retrieval strategies
- UI enhancements and improved interaction flow
- CI integration for automated testing

---

## 📸 Demo

![Home Page](screenshots/home.png)
![Study Interface](screenshots/study.png)

---


## 📝 License

This project is licensed under the MIT License.
