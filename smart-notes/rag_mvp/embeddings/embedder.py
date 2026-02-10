"""
Embedding wrapper for converting text chunks into vectors.
Supports pluggable embedding backends later (Ollama, OpenAI, SentenceTransformers).
"""

from typing import List
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None


class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        if SentenceTransformer is None:
            raise ImportError(
                "sentence-transformers not installed. Run: pip install sentence-transformers"
            )

        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> np.ndarray:
        if not texts:
            return np.array([])

        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
