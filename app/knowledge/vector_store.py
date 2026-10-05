import faiss

from app.knowledge.chunking import chunk_documents
from app.knowledge.embeddings import generate_embeddings


class KnowledgeVectorStore:
    """
    Local FAISS vector store for semantic knowledge retrieval.

    The store keeps the original chunk metadata alongside the FAISS
    index so retrieved content can be traced back to its source.
    """

    def __init__(self):
        self.chunks = chunk_documents()

        texts = [
            chunk["content"]
            for chunk in self.chunks
        ]

        embeddings = generate_embeddings(texts)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

    def search(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[dict]:
        """
        Returns the most semantically relevant knowledge chunks.
        """

        query_embedding = generate_embeddings([query])

        scores, indices = self.index.search(
            query_embedding,
            min(top_k, len(self.chunks)),
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0],
        ):
            if index < 0:
                continue

            chunk = self.chunks[index].copy()

            chunk["similarity_score"] = float(score)

            results.append(chunk)

        return results