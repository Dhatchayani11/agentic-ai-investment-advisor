from app.orchestration.state import InvestmentAdvisorState


PROHIBITED_TERMS = [
    "guaranteed return",
    "guaranteed profit",
    "risk-free investment",
    "you will definitely make money",
]


REGULATORY_INDICATORS = [
    "$",
    "%",
    "401(k)",
    "ira",
    "contribution limit",
    "tax penalty",
    "penalty",
    "catch-up contribution",
]


def compliance_agent(
    state: InvestmentAdvisorState,
) -> InvestmentAdvisorState:
    """
    Performs an initial compliance assessment of the proposed analysis.

    The prototype checks:
    1. Prohibited investment claims.
    2. Potentially unsupported regulatory facts or figures.

    The reason for a review decision is stored separately so that
    monitoring and evaluation can identify why the response was flagged.
    """

    analysis = state.get("financial_analysis", "")
    knowledge = state.get("knowledge_context", "")

    analysis_lower = analysis.lower()

    prohibited_found = any(
        term in analysis_lower
        for term in PROHIBITED_TERMS
    )

    contains_regulatory_information = any(
        indicator.lower() in analysis_lower
        for indicator in REGULATORY_INDICATORS
    )

    unsupported_regulatory_information = (
        contains_regulatory_information
        and (
            not knowledge
            or knowledge == "No relevant policy knowledge was found."
        )
    )

    if prohibited_found:
        state["compliance_result"] = "REQUIRES_REVIEW"
        state["compliance_reason"] = (
            "Prohibited investment claim detected."
        )

    elif unsupported_regulatory_information:
        state["compliance_result"] = "REQUIRES_REVIEW"
        state["compliance_reason"] = (
            "Regulatory information detected without "
            "sufficient supporting knowledge."
        )

    else:
        state["compliance_result"] = "PASSED"
        state["compliance_reason"] = (
            "No prohibited claims or unsupported regulatory "
            "information detected."
        )

    return state