import json

import pytest

from app.monitoring import feedback


def test_record_positive_feedback(tmp_path, monkeypatch):
    feedback_file = tmp_path / "feedback.jsonl"

    monkeypatch.setattr(
        feedback,
        "FEEDBACK_FILE",
        feedback_file,
    )

    feedback_id = feedback.record_feedback(
        advice_id="advice-001",
        customer_id="customer-001",
        rating="positive",
        comment="The explanation was clear.",
    )

    assert feedback_id

    record = json.loads(
        feedback_file.read_text(encoding="utf-8").strip()
    )

    assert record["feedback_id"] == feedback_id
    assert record["advice_id"] == "advice-001"
    assert record["customer_id"] == "customer-001"
    assert record["rating"] == "positive"
    assert record["comment"] == "The explanation was clear."


def test_record_negative_feedback(tmp_path, monkeypatch):
    feedback_file = tmp_path / "feedback.jsonl"

    monkeypatch.setattr(
        feedback,
        "FEEDBACK_FILE",
        feedback_file,
    )

    feedback_id = feedback.record_feedback(
        advice_id="advice-002",
        customer_id="customer-002",
        rating="negative",
    )

    assert feedback_id

    record = json.loads(
        feedback_file.read_text(encoding="utf-8").strip()
    )

    assert record["rating"] == "negative"
    assert record["comment"] is None


def test_invalid_feedback_rating_is_rejected():
    with pytest.raises(ValueError, match="Rating must be either"):
        feedback.record_feedback(
            advice_id="advice-003",
            customer_id="customer-003",
            rating="neutral",
        )