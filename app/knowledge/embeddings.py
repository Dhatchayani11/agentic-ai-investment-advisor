from sentence_transformers import SentenceTransformer


EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


_embedding_model = SentenceTransformer(
    EMBEDDING_MODEL_NAME
)


def generate_embeddings(
    texts: list[str],
):
    """
    Generates semantic embeddings for knowledge chunks.

    MiniLM produces 384-dimensional embeddings that are suitable
    for a lightweight local RAG prototype.
    """

    if not texts:
        return []

    return _embedding_model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )