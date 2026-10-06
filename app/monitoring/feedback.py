import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


FEEDBACK_FILE = Path("app/monitoring/feedback.jsonl")

VALID_RATINGS = {
    "positive",
    "negative",
}


def record_feedback(
    *,
    advice_id: str,
    customer_id: str,
    rating: str,
    comment: str | None = None,
) -> str:
    """
    Stores customer or reviewer feedback for a generated response.

    JSONL is used for the prototype so each feedback record is
    independently stored and can later be migrated to a database
    or cloud event stream.
    """

    normalized_rating = rating.strip().lower()

    if normalized_rating not in VALID_RATINGS:
        raise ValueError(
            "Rating must be either 'positive' or 'negative'."
        )

    feedback_id = str(uuid4())

    feedback_record = {
        "feedback_id": feedback_id,
        "advice_id": advice_id,
        "customer_id": customer_id,
        "rating": normalized_rating,
        "comment": comment,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    FEEDBACK_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with FEEDBACK_FILE.open(
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            json.dumps(feedback_record)
            + "\n"
        )

    return feedback_id