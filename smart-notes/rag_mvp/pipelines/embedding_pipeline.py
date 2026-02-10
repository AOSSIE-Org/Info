# rag_mvp/pipelines/embedding_pipeline.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class EmbeddingPipeline:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name, cache_folder="D:/models_cache")
        self.index = None
        self.chunks = []

    def chunk_text(self, text, max_length=300, overlap=50):
        chunks = []
        start = 0

        while start < len(text):
            end = start + max_length
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap

        return chunks

    def build_index(self, chunks):
        embeddings = self.model.encode(chunks)
        embeddings = np.array(embeddings).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

        return embeddings

    def process_notes(self, text):
        self.chunks = self.chunk_text(text)
        embeddings = self.build_index(self.chunks)
        return self.chunks, embeddings

    def semantic_search(self, query, top_k=3):
        query_vec = self.model.encode([query])
        query_vec = np.array(query_vec).astype("float32")

        distances, indices = self.index.search(query_vec, top_k)
        results = [self.chunks[i] for i in indices[0]]
        return results
