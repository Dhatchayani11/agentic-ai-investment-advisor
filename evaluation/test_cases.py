EVALUATION_CASES = [
    {
        "id": "RETIREMENT_001",
        "query": "Should I increase my retirement contribution?",
        "expected_intent": "RETIREMENT_PLANNING",
        "expected_compliance": "PASSED",
        "reference_answer": (
            "Increasing retirement contributions may increase long-term "
            "retirement savings but can reduce current disposable income. "
            "The decision depends on financial circumstances, retirement "
            "goals, liquidity needs, applicable account rules, and employer "
            "plan terms."
        ),
        "expected_knowledge_terms": [
            "retirement",
            "contributions",
            "financial circumstances",
            "retirement goals",
        ],
    },
    {
        "id": "STOCK_001",
        "query": "Should I invest in stocks?",
        "expected_intent": "STOCK_INVESTMENT",
        "expected_compliance": "REQUIRES_REVIEW",
        "reference_answer": (
            "Stock investments can fluctuate in value and may involve "
            "significant risk. Investment decisions should consider the "
            "customer's goals, financial circumstances, liquidity needs, "
            "and risk tolerance."
        ),
        "expected_knowledge_terms": [
            "investment",
            "risk",
            "financial circumstances",
        ],
    },
    {
        "id": "GENERAL_001",
        "query": "What are some general investment options?",
        "expected_intent": "GENERAL_INVESTMENT",
        "expected_compliance": "REQUIRES_REVIEW",
        "reference_answer": (
            "General investment options can have different levels of risk, "
            "return potential, and liquidity. The appropriate information "
            "depends on the customer's goals and financial circumstances."
        ),
        "expected_knowledge_terms": [
            "investment",
            "risk",
            "financial circumstances",
        ],
    },
]