from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_high_risk():
    response = client.post("/analyze-risk", json={
        "summary": "login con validación"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "alto"


def test_medium_risk():
    response = client.post("/analyze-risk", json={
        "summary": "formulario de contacto"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "medio"


def test_low_risk():
    response = client.post("/analyze-risk", json={
        "summary": "cambio de texto en label"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "bajo"