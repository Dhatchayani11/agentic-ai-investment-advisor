from langgraph.graph import StateGraph, START, END

from app.orchestration.state import InvestmentAdvisorState
from app.agents.intent_agent import intent_agent
from app.agents.investment_agent import investment_agent
from app.agents.compliance_agent import compliance_agent
from app.agents.fairness_agent import fairness_agent
from app.agents.response_agent import response_agent

def build_investment_advisor_graph():
    workflow = StateGraph(InvestmentAdvisorState)

    workflow.add_node("intent_agent", intent_agent)
    workflow.add_node("investment_agent", investment_agent)
    workflow.add_node("compliance_agent", compliance_agent)
    workflow.add_node("fairness_agent", fairness_agent)
    workflow.add_node("response_agent", response_agent)

    workflow.add_edge(START, "intent_agent")
    workflow.add_edge("intent_agent", "investment_agent")
    workflow.add_edge("investment_agent", "compliance_agent")
    workflow.add_edge("compliance_agent", "fairness_agent")
    workflow.add_edge("fairness_agent", "response_agent")
    workflow.add_edge("response_agent", END)

    return workflow.compile()


investment_advisor_graph = build_investment_advisor_graph()


if __name__ == "__main__":
    result = investment_advisor_graph.invoke(
        {
            "customer_id": "customer-001",
            "query": "Should I increase my pension contribution?"
        }
    )

    print(result)