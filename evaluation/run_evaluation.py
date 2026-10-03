import time

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

    print("\n--- Evaluation Results ---")

    for result in results:
        print(result)

    print("\n--- Evaluation Metrics ---")
    print(f"Intent accuracy: {intent_accuracy:.2f}%")
    print(f"Compliance accuracy: {compliance_accuracy:.2f}%")
    print(
        f"Regulatory fact safety rate: "
        f"{regulatory_fact_safety_rate:.2f}%"
    )
    print(f"Fairness pass rate: {fairness_rate:.2f}%")
    print(f"Explanation coverage: {explanation_rate:.2f}%")
    print(f"Response coverage: {response_rate:.2f}%")
    print(f"Average latency: {average_latency:.2f} ms")


if __name__ == "__main__":
    run_evaluation()