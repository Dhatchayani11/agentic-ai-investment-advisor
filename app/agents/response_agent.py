from app.llm_service import get_llm
from app.orchestration.state import InvestmentAdvisorState
from app.prompts.investment_prompts import (
    RESPONSE_PROMPT,
    RESPONSE_PROMPT_VERSION,
)


def response_agent(
    state: InvestmentAdvisorState,
) -> InvestmentAdvisorState:
    """
    Generates the final customer-facing response.

    The response is generated only after compliance and fairness checks
    have passed. The final response must remain educational and must not
    make a definitive personalized investment recommendation.
    """

    compliance = state.get(
        "compliance_result",
        "REQUIRES_REVIEW",
    )

    fairness = state.get(
        "fairness_result",
        "REQUIRES_REVIEW",
    )

    # Do not generate customer-facing investment guidance when
    # a mandatory validation check has failed.
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
        financial_analysis=state.get(
            "financial_analysis",
            "",
        ),
        compliance_result=compliance,
        fairness_result=fairness,
    )

    response = llm.invoke(prompt)

    final_response = response.content

    # Store the response prompt version for traceability.
    state["response_prompt_version"] = RESPONSE_PROMPT_VERSION

    # Defense-in-depth check:
    # Prevent the final response from directly recommending an
    # investment action even if the LLM produces recommendation language.
    recommendation_phrases = [
        "you should increase",
        "you should invest",
        "you should contribute",
        "i recommend increasing",
        "i recommend investing",
        "i recommend contributing",
        "you should definitely",
        "you should consider increasing",
    ]

    response_lower = final_response.lower()

    if any(
        phrase in response_lower
        for phrase in recommendation_phrases
    ):
        state["final_response"] = (
            "The available information is not sufficient to provide "
            "a personalized investment recommendation. Please review "
            "your retirement goals, contribution limits, employer plan "
            "rules, cash-flow needs, and other relevant circumstances "
            "before making a decision."
        )
    else:
        state["final_response"] = final_response

    knowledge_context = state.get(
        "knowledge_context",
        "",
    )

    source_line = "No policy knowledge was retrieved."

    if (
        knowledge_context
        and knowledge_context
        != "No relevant policy knowledge was found."
    ):
        source_line = (
            "Relevant policy knowledge was retrieved and used "
            "as grounding context."
        )

    state["explanation"] = (
        "The customer query was analyzed using retrieved policy "
        "knowledge and reviewed through compliance and fairness "
        "checks before generating the final response. "
        f"{source_line}"
    )

    return state