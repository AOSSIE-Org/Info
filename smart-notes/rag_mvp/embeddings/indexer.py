"""
Simple vector indexer using FAISS for similarity search.
"""

from typing import List
import numpy as np

try:
    import faiss
except ImportError:
    faiss = None


class VectorIndexer:
    def __init__(self, dim: int):
        if faiss is None:
            raise ImportError("faiss not installed. Run: pip install faiss-cpu")

        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts: List[str] = []

    def add(self, embeddings: np.ndarray, chunks: List[str]):
        if len(embeddings) == 0:
            return

        self.index.add(embeddings)
        self.texts.extend(chunks)

    def search(self, query_embedding: np.ndarray, k: int = 3):
        if self.index.ntotal == 0:
            return []

        distances, indices = self.index.search(query_embedding.reshape(1, -1), k)
        results = []

        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])

        return results
