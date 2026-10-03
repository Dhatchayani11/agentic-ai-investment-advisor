"""
Evaluation dataset for the AI Investment Advisor.

The dataset is used to evaluate:
- Intent accuracy
- Compliance
- Regulatory fact safety
- Fairness
- Explainability
- Response generation
- Latency
"""

EVALUATION_CASES = [
    {
        "id": "RETIREMENT_001",
        "query": "Should I increase my retirement contribution?",
        "expected_intent": "RETIREMENT_PLANNING",
        "expected_compliance": "PASSED",
    },
    {
        "id": "STOCK_001",
        "query": "Should I invest in stocks?",
        "expected_intent": "STOCK_INVESTMENT",
        "expected_compliance": "PASSED",
    },
    {
        "id": "GENERAL_001",
        "query": "What are some general investment options?",
        "expected_intent": "GENERAL_INVESTMENT",
        "expected_compliance": "PASSED",
    },
]