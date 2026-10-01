from app.orchestration.state import InvestmentAdvisorState


def response_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Generates the final customer-facing response.

    This is currently a deterministic implementation.
    The LLM-based response generation will be added after
    the complete agent workflow is validated.
    """

    intent = state.get("intent", "UNKNOWN")
    analysis = state.get("financial_analysis", "")
    compliance = state.get("compliance_result", "REQUIRES_REVIEW")
    fairness = state.get("fairness_result", "REQUIRES_REVIEW")

    # Do not generate a customer-facing recommendation when
    # a mandatory safety check has failed.
    if compliance != "PASSED" or fairness != "PASSED":
        state["final_response"] = (
            "This investment query requires additional review "
            "before personalized guidance can be provided."
        )

        state["explanation"] = (
            f"Compliance status: {compliance}. "
            f"Fairness status: {fairness}."
        )

        return state

    state["final_response"] = (
        "Your question relates to retirement planning and pension "
        "contributions. Increasing a pension contribution may affect "
        "your long-term retirement savings, but the appropriate amount "
        "depends on your individual financial circumstances and goals. "
        "Consider the relevant pension rules, employer contribution "
        "arrangements, and your retirement objectives before making a change."
    )

    state["explanation"] = (
        f"Intent identified as {intent}. "
        f"The investment analysis was reviewed by the compliance "
        f"and fairness checks before generating the response."
    )

    return state