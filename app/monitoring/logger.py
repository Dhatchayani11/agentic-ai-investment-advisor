import logging
from app.prompts.investment_prompts import (
    INVESTMENT_PROMPT_DEFINITION,
    RESPONSE_PROMPT_DEFINITION,
)

logger = logging.getLogger("investment_advisor")

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def log_workflow_result(
    *,
    customer_id: str,
    query: str,
    result: dict,
    latency_ms: float,
) -> None:
    """
    Records operational and AI workflow metrics.

    Customer query content is intentionally not logged in full
    to reduce unnecessary exposure of potentially sensitive data.
    """

    knowledge_retrieved = bool(
        result.get("knowledge_context")
        and result.get("knowledge_context")
        != "No relevant policy knowledge was found."
    )

    logger.info(
        "workflow_completed | "
        "customer_id=%s | "
        "latency_ms=%.2f | "
        "intent=%s | "
        "compliance=%s | "
        "compliance_reason=%s | "
        "fairness=%s | "
        "prompt_version=%s | "
        "response_prompt_version=%s | "
        "knowledge_retrieved=%s",
        "prompt_hash=%s | "
        "response_prompt_hash=%s | "
        customer_id,
        latency_ms,
        result.get("intent"),
        result.get("compliance_result"),
        result.get("compliance_reason"),
        result.get("fairness_result"),
        result.get("prompt_version"),
        result.get("response_prompt_version"),
        knowledge_retrieved,
        INVESTMENT_PROMPT_DEFINITION.content_hash,
        RESPONSE_PROMPT_DEFINITION.content_hash,
    )