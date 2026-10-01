from fastapi import FastAPI

from app.models import InvestmentQuery, InvestmentResponse

app = FastAPI(
    title="Agentic AI Investment Advisor",
    description="Multi-agent AI system for personalized and compliant investment guidance",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/investment/advice", response_model=InvestmentResponse)
def investment_advice(request: InvestmentQuery):
    """
    Initial API endpoint.

    Agent orchestration will be added in the next stage.
    """
    return InvestmentResponse(
        response="Investment analysis will be generated here.",
        explanation="Agent-based analysis is not implemented yet.",
        compliance_status="PENDING",
    )