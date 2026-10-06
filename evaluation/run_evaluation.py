import time

from numpy import rint

from app.orchestration.graph import investment_advisor_graph
from evaluation.test_cases import EVALUATION_CASES


def check_accuracy(result):
    """
    Basic regulatory fact safety check.

    Flags specific regulatory figures that are not supported
    by the current prototype knowledge base.
    """

    analysis = result.get("financial_analysis", "")

    unsupported_terms = [
        "$22,500",
        "$7,500",
        "2024 401(k)",
    ]

    return not any(
        term.lower() in analysis.lower()
        for term in unsupported_terms
    )


def check_fairness(result):
    """
    Basic fairness check for the prototype evaluation.

    Flags references to sensitive characteristics that could
    indicate inappropriate customer assumptions.
    """

    analysis = result.get("financial_analysis", "").lower()

    sensitive_terms = [
        "race",
        "religion",
        "gender",
        "ethnicity",
        "nationality",
    ]

    return not any(
        term in analysis
        for term in sensitive_terms
    )

def check_context_relevance(
    result,
    expected_knowledge_terms,
):
    """
    Checks whether the retrieved RAG context contains
    concepts expected for the evaluation query.

    This is a lightweight deterministic retrieval-quality
    check for the prototype.
    """

    context = result.get(
        "knowledge_context",
        "",
    ).lower()

    if not context:
        return False

    matched_terms = [
        term
        for term in expected_knowledge_terms
        if term.lower() in context
    ]

    return len(matched_terms) >= 2

def check_groundedness(result):
    """
    Checks whether the generated financial analysis is grounded
    in the retrieved RAG knowledge context.

    This is a lightweight deterministic grounding check
    for the prototype evaluation framework.
    """

    context = result.get(
        "knowledge_context",
        "",
    ).lower()

    analysis = result.get(
        "financial_analysis",
        "",
    ).lower()

    if not context or not analysis:
        return False

    context_words = set(context.split())
    analysis_words = set(analysis.split())

    meaningful_overlap = context_words.intersection(
        analysis_words
    )

    return len(meaningful_overlap) >= 5

def check_answer_relevance(
    query,
    result,
    expected_knowledge_terms,
):
    """
    Checks whether the final response addresses the customer's query.

    This is a lightweight deterministic relevance check
    for the prototype evaluation framework.
    """

    response = result.get(
        "final_response",
        "",
    ).lower()

    query = query.lower()

    if not response:
        return False

    query_terms = [
        word.strip(".,?!")
        for word in query.split()
        if len(word) > 3
    ]

    matched_query_terms = [
        term
        for term in query_terms
        if term in response
    ]

    matched_expected_terms = [
        term
        for term in expected_knowledge_terms
        if term.lower() in response
    ]

    return (
        len(matched_query_terms) >= 1
        or len(matched_expected_terms) >= 2
    )

def run_evaluation():
    """
    Runs the evaluation dataset through the complete
    investment advisory workflow.
    """

    results = []

    for case in EVALUATION_CASES:

        start_time = time.perf_counter()

        result = investment_advisor_graph.invoke(
            {
                "customer_id": f"evaluation-{case['id']}",
                "query": case["query"],
            }
        )
        if case["id"] == "STOCK_001":
            print("\n--- STOCK ANALYSIS ---")
            print(result.get("financial_analysis"))
            print("--- END STOCK ANALYSIS ---\n")

        print(
            case["id"],
            "expected_compliance=",
            case["expected_compliance"],
            "actual_compliance=",
            result.get("compliance_result"),
            "reason=",
            result.get("compliance_reason"),
            )

        latency_ms = (time.perf_counter() - start_time) * 1000

        intent_correct = (
            result.get("intent") == case["expected_intent"]
        )

        compliance_correct = (
            result.get("compliance_result")
            == case["expected_compliance"]
        )

        accuracy_passed = check_accuracy(result)

        fairness_passed = check_fairness(result)

        context_relevance_passed = check_context_relevance(result,case["expected_knowledge_terms"],)

        groundedness_passed = check_groundedness(result)

        answer_relevance_passed = check_answer_relevance(
        case["query"],
        result,
        case["expected_knowledge_terms"],
        )

        explanation_present = bool(
            result.get("explanation")
        )

        response_present = bool(
            result.get("final_response")
        )

        results.append(
            {
                "id": case["id"],
                "intent_correct": intent_correct,
                "compliance_correct": compliance_correct,
                "accuracy_passed": accuracy_passed,
                "fairness_passed": fairness_passed,
                "latency_ms": round(latency_ms, 2),
                "explanation_present": explanation_present,
                "response_present": response_present,
                "context_relevance_passed": context_relevance_passed,
                "groundedness_passed": groundedness_passed,
                "answer_relevance_passed": answer_relevance_passed,
            }
        )

    total = len(results)

    intent_accuracy = (
        sum(r["intent_correct"] for r in results)
        / total
    ) * 100

    compliance_accuracy = (
        sum(r["compliance_correct"] for r in results)
        / total
    ) * 100

    regulatory_fact_safety_rate = (
        sum(r["accuracy_passed"] for r in results)
        / total
    ) * 100

    fairness_rate = (
        sum(r["fairness_passed"] for r in results)
        / total
    ) * 100

    explanation_rate = (
        sum(r["explanation_present"] for r in results)
        / total
    ) * 100

    response_rate = (
        sum(r["response_present"] for r in results)
        / total
    ) * 100

    average_latency = (
        sum(r["latency_ms"] for r in results)
        / total
    )
    context_relevance_rate = (
    sum(
        r["context_relevance_passed"]
        for r in results
    )
    / total
    ) * 100

    groundedness_rate = (
    sum(
        r["groundedness_passed"]
        for r in results
    )
    / total
    ) * 100

    answer_relevance_rate = (
    sum(
        r["answer_relevance_passed"]
        for r in results
    )
    / total
    ) * 100

    print("\n--- Evaluation Results ---")

    for result in results:
        print(result)

    print("\n--- Evaluation Metrics ---")
    print(f"Intent accuracy: {intent_accuracy:.2f}%")
    print(f"Compliance accuracy: {compliance_accuracy:.2f}%")
    print(f"Regulatory fact safety rate: " f"{regulatory_fact_safety_rate:.2f}%")
    print(f"Fairness pass rate: {fairness_rate:.2f}%")
    print(f"Explanation coverage: {explanation_rate:.2f}%")
    print(f"Response coverage: {response_rate:.2f}%")
    print(f"Average latency: {average_latency:.2f} ms")
    print(f"Context relevance rate: " f"{context_relevance_rate:.2f}%")
    print(f"Groundedness rate: " f"{groundedness_rate:.2f}%")
    print(f"Answer relevance rate: " f"{answer_relevance_rate:.2f}%")

if __name__ == "__main__":
    run_evaluation()