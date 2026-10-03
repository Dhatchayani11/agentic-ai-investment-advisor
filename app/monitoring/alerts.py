import logging


logger = logging.getLogger("investment_advisor.alerts")


LATENCY_THRESHOLD_MS = 30000


def check_alert_conditions(
    *,
    result: dict,
    latency_ms: float,
) -> None:
    """
    Checks workflow results against operational and
    safety alert thresholds.
    """

    if latency_ms > LATENCY_THRESHOLD_MS:
        logger.warning(
            "ALERT | High latency detected | latency_ms=%.2f",
            latency_ms,
        )

    if result.get("compliance_result") == "REQUIRES_REVIEW":
        logger.warning(
            "ALERT | Compliance review required | reason=%s",
            result.get(
                "compliance_reason",
                "No compliance reason provided.",
            ),
        )

    if result.get("fairness_result") == "REQUIRES_REVIEW":
        logger.warning(
            "ALERT | Fairness review required"
        )