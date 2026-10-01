from app.orchestration.state import InvestmentAdvisorState


def intent_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Identifies the customer's investment-related intent.

    This is currently a deterministic placeholder.
    LLM-based intent classification will be introduced
    after the orchestration structure is validated.
    """

    query = state["query"].lower()

    if "pension" in query or "retirement" in query:
        intent = "RETIREMENT_PLANNING"

    elif "stock" in query or "share" in query:
        intent = "STOCK_INVESTMENT"

    elif "investment" in query:
        intent = "GENERAL_INVESTMENT"

    else:
        intent = "UNKNOWN"

    state["intent"] = intent

    return state