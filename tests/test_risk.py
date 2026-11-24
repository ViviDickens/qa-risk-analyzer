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

def test_api_inside_another_word_is_not_high_risk():
    response = client.post("/analyze-risk", json={
        "summary": "cambio de texto en capital"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "bajo"


def test_english_payment_is_high_risk():
    response = client.post("/analyze-risk", json={
        "summary": "Payment page redesign"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "alto"


def test_accent_and_uppercase_are_ignored():
    response = client.post("/analyze-risk", json={
        "summary": "VALIDACIÓN de campos"
    })
    assert response.status_code == 200
    assert response.json()["risk"] == "medio"


def test_empty_summary_returns_422():
    response = client.post("/analyze-risk", json={"summary": ""})
    assert response.status_code == 422


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
