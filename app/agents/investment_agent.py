from app.orchestration.state import InvestmentAdvisorState


def investment_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Analyzes the investment context identified by the intent agent.

    This initial implementation establishes the agent interface.
    Financial knowledge/RAG and LLM reasoning will be added next.
    """

    intent = state.get("intent", "UNKNOWN")

    if intent == "RETIREMENT_PLANNING":
        analysis = (
            "The query relates to retirement planning and pension contributions."
        )
    elif intent == "STOCK_INVESTMENT":
        analysis = (
            "The query relates to stock or share investment."
        )
    elif intent == "GENERAL_INVESTMENT":
        analysis = (
            "The query relates to general investment guidance."
        )
    else:
        analysis = (
            "The investment intent could not be determined."
        )

    state["financial_analysis"] = analysis

    return state