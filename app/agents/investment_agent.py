from app.llm_service import get_llm
from app.orchestration.state import InvestmentAdvisorState
from app.prompts.investment_prompts import (
    INVESTMENT_ANALYSIS_PROMPT,
    PROMPT_VERSION,
)


def investment_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Uses the LLM to analyze the customer's investment question.

    The prompt is maintained separately to support prompt
    versioning and lifecycle management.
    """

    llm = get_llm()

    prompt = INVESTMENT_ANALYSIS_PROMPT.format(
        query=state["query"],
        intent=state.get("intent", "UNKNOWN"),
    )

    response = llm.invoke(prompt)

    state["financial_analysis"] = response.content

    # Store the prompt version for traceability and evaluation.
    state["prompt_version"] = PROMPT_VERSION

    return state