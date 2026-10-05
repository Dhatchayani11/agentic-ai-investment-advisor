from app.knowledge.ingestion import ingest_documents


MIN_CHUNK_LENGTH = 40


def chunk_documents() -> list[dict]:
    """
    Splits ingested knowledge documents into meaningful retrievable chunks.

    Very short headings or metadata-only sections are excluded because
    they do not contain enough information to support retrieval.
    """

    documents = ingest_documents()

    chunks = []

    for document in documents:
        sections = document["content"].split("\n\n")

        chunk_index = 0

        for section in sections:
            content = section.strip()

            if not content:
                continue

            if len(content) < MIN_CHUNK_LENGTH:
                continue

            chunks.append(
                {
                    "chunk_id": (
                        f"{document['document_name']}"
                        f"::chunk-{chunk_index}"
                    ),
                    "document_name": document["document_name"],
                    "document_type": document["document_type"],
                    "content": content,
                }
            )

            chunk_index += 1

    return chunks