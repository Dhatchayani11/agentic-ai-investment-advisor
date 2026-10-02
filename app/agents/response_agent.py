from app.llm_service import get_llm
from app.orchestration.state import InvestmentAdvisorState
from app.prompts.investment_prompts import (
    RESPONSE_PROMPT,
    RESPONSE_PROMPT_VERSION,
)


def response_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Generates the final customer-facing response using the LLM.

    The response is generated only after the compliance and
    fairness agents have completed their checks.
    """

    compliance = state.get("compliance_result", "REQUIRES_REVIEW")
    fairness = state.get("fairness_result", "REQUIRES_REVIEW")

    # Do not generate personalized guidance when a mandatory
    # validation check has failed.
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

    llm = get_llm()

    prompt = RESPONSE_PROMPT.format(
        query=state["query"],
        financial_analysis=state.get("financial_analysis", ""),
        compliance_result=compliance,
        fairness_result=fairness,
    )

    response = llm.invoke(prompt)

    state["final_response"] = response.content

    state["response_prompt_version"] = RESPONSE_PROMPT_VERSION

    return state