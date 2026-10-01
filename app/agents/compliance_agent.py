from app.orchestration.state import InvestmentAdvisorState


def compliance_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Performs an initial compliance assessment of the proposed analysis.

    This is a rule-based placeholder. In the complete system, this agent
    will use approved regulatory/policy knowledge through RAG and an LLM,
    with deterministic validation for critical rules.
    """

    query = state["query"].lower()
    analysis = state.get("financial_analysis", "")

    # Basic safety check for unsupported guaranteed-return claims.
    prohibited_terms = [
        "guaranteed return",
        "guaranteed profit",
        "risk-free investment",
        "you will definitely make money",
    ]

    if any(term in analysis.lower() for term in prohibited_terms):
        compliance_status = "REQUIRES_REVIEW"
    else:
        compliance_status = "PASSED"

    state["compliance_result"] = compliance_status

    return state