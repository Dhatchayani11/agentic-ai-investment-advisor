from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_feedback_api_rejects_invalid_rating():
    response = client.post(
        "/investment/feedback",
        json={
            "advice_id": "advice-001",
            "customer_id": "customer-001",
            "rating": "neutral",
            "comment": "Testing invalid rating",
        },
    )

    assert response.status_code == 422