from app.knowledge.vector_store import KnowledgeVectorStore


_vector_store = KnowledgeVectorStore()
SIMILARITY_THRESHOLD = 0.50

def retrieve_knowledge(
    query: str,
    top_k: int = 3,
) -> str:
    """
    Retrieves semantically relevant knowledge for the customer query.

    The retrieved source metadata is preserved so downstream agents
    can trace the knowledge used to ground the response.
    """

    results = _vector_store.search(
        query=query,
        top_k=top_k,
    )
    results = [
        result
        for result in results
        if result["similarity_score"] >= SIMILARITY_THRESHOLD
    ]

    if not results:
        return "No relevant policy knowledge was found."

    formatted_results = []

    for result in results:
        formatted_results.append(
            f"Source document: {result['document_name']}\n"
            f"Document type: {result['document_type']}\n"
            f"Similarity score: "
            f"{result['similarity_score']:.4f}\n"
            f"{result['content']}"
        )

    return "\n\n".join(formatted_results)