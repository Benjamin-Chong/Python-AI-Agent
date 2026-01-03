from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/ask", json = {"question": "What is a variable?"})

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert isinstance(data["answer"], str)

