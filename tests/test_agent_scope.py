from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_out_of_scope():
    response = client.post("/ask", json = {"question" : "What is the max overclock for a Ryzen 7600X?"})

    answer = response.json()["answer"].lower()
    assert "i do not know" in answer

def test_question_answered_from_notes():
    response = client.post(
        "/ask",
        json={"question": "What is the difference between a for loop and a while loop?"}
    )

    assert response.status_code == 200
    answer = response.json()["answer"].lower()

    assert "for loop" in answer
    assert "while loop" in answer
