from pathlib import Path


KNOWLEDGE_DIR = Path(__file__).parent / "documents"


def ingest_documents() -> list[dict]:
    """
    Loads knowledge documents used by the investment advisory system.

    Document metadata is separated from the actual knowledge sections
    so retrieval only operates on meaningful guidance content.
    """

    documents = []

    for document_path in KNOWLEDGE_DIR.glob("*.txt"):
        content = document_path.read_text(
            encoding="utf-8"
        ).strip()

        if not content:
            continue

        sections = content.split("\n\n")

        knowledge_sections = []

        for section in sections:
            section = section.strip()

            # Skip document-level metadata.
            if section.startswith("Source:"):
                continue

            if section.startswith("Document type:"):
                continue

            if section.startswith("Authoritative source:"):
                continue

            if section.startswith("Source verification date:"):
                continue

            if section.startswith("Purpose:"):
                continue

            if section.startswith("Compliance principle:"):
                continue

            if section.startswith("Regulatory source principle:"):
                continue

            if section == "RETIREMENT CONTRIBUTION GUIDANCE":
                continue

            knowledge_sections.append(section)

        documents.append(
            {
                "document_name": document_path.name,
                "document_type": "policy_guidance",
                "content": "\n\n".join(knowledge_sections),
            }
        )

    return documents