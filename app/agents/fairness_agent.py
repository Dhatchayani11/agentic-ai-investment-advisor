from app.orchestration.state import InvestmentAdvisorState


def fairness_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Performs an initial fairness assessment.

    The prototype checks whether the response contains assumptions
    based on protected or sensitive customer characteristics.

    A production implementation would use a dedicated fairness
    evaluation framework and representative test datasets.
    """

    analysis = state.get("financial_analysis", "")

    sensitive_terms = [
        "race",
        "religion",
        "gender",
        "ethnicity",
        "nationality",
    ]

    detected_terms = [
        term for term in sensitive_terms
        if term in analysis.lower()
    ]

    if detected_terms:
        state["fairness_result"] = "REQUIRES_REVIEW"
    else:
        state["fairness_result"] = "PASSED"

    return state