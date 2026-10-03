from app.knowledge.ingestion import ingest_documents


STOP_WORDS = {
    "the",
    "should",
    "i",
    "my",
    "a",
    "an",
    "is",
    "are",
    "to",
    "in",
    "of",
    "for",
    "and",
    "or",
    "can",
    "could",
    "would",
    "what",
    "how",
}


def retrieve_knowledge(query: str) -> str:
    """
    Retrieves relevant knowledge sections from ingested documents.

    The prototype uses keyword overlap with stop-word filtering.
    Semantic/vector retrieval can replace this implementation later
    without changing the ingestion interface.
    """

    query_terms = {
        term.strip(".,?!").lower()
        for term in query.split()
        if len(term.strip(".,?!")) > 2
        and term.strip(".,?!").lower() not in STOP_WORDS
    }

    relevant_sections = []

    documents = ingest_documents()

    for document in documents:
        content = document["content"]

        sections = content.split("\n\n")

        for section in sections:
            section_clean = section.strip()

            if not section_clean:
                continue

            section_terms = {
                term.strip(".,?!:").lower()
                for term in section_clean.split()
                if len(term.strip(".,?!:")) > 2
            }

            matched_terms = query_terms.intersection(section_terms)

            if not matched_terms:
                continue

            relevant_sections.append(
                {
                    "document_name": document["document_name"],
                    "document_type": document["document_type"],
                    "section": section_clean,
                    "score": len(matched_terms),
                }
            )

    if not relevant_sections:
        return "No relevant policy knowledge was found."

    # Return the most relevant sections first.
    relevant_sections.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    formatted_sections = []

    for item in relevant_sections[:5]:
        formatted_sections.append(
            f"Source document: {item['document_name']}\n"
            f"Document type: {item['document_type']}\n"
            f"{item['section']}"
        )

    return "\n\n".join(formatted_sections)