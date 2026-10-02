from typing import TypedDict


class InvestmentAdvisorState(TypedDict, total=False):
    """
    Shared state passed between agents in the investment advisory workflow.
    """

    customer_id: str
    query: str

    intent: str
    financial_analysis: str
    compliance_result: str
    fairness_result: str
    prompt_version: str
    response_prompt_version: str
    final_response: str
    explanation: str

    