from app.llm_service import get_llm
from app.knowledge.retriever import retrieve_knowledge
from app.orchestration.state import InvestmentAdvisorState
from app.prompts.investment_prompts import (
    INVESTMENT_ANALYSIS_PROMPT,
    PROMPT_VERSION,
)


def investment_agent(state: InvestmentAdvisorState) -> InvestmentAdvisorState:
    """
    Analyzes the customer's investment question using
    retrieved policy knowledge as grounding context.
    """

    llm = get_llm()

    knowledge = retrieve_knowledge(state["query"])
    state["knowledge_context"] = knowledge

    prompt = INVESTMENT_ANALYSIS_PROMPT.format(
        query=state["query"],
        intent=state.get("intent", "UNKNOWN"),
        knowledge=knowledge,
    )

    response = llm.invoke(prompt)

    state["financial_analysis"] = response.content

    # Store the prompt version for traceability and evaluation.
    state["prompt_version"] = PROMPT_VERSION

    return state