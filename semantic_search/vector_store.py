from typing import List, Dict, Any
import faiss
import numpy as np


class VectorStore:
    """
    Simple FAISS-based vector store for semantic search.
    """

    def __init__(self, embedding_dim: int):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.metadata: List[Dict[str, Any]] = []

    def add(self, embeddings: List[List[float]], metadatas: List[Dict[str, Any]]):
        """
        Add embeddings and corresponding metadata to the index.
        """
        if len(embeddings) != len(metadatas):
            raise ValueError("Embeddings and metadata length mismatch")

        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(metadatas)

    def search(self, query_embedding: List[float], k: int = 5):
        """
        Search for the top-k most similar embeddings.
        """
        query_vector = np.array([query_embedding]).astype("float32")
        scores, indices = self.index.search(query_vector, k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            result = self.metadata[idx].copy()
            result["score"] = float(score)
            results.append(result)

        return results
