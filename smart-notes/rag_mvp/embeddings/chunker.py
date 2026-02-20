"""
Chunking utilities for splitting long notes into overlapping chunks.
This helps embeddings capture local context.
"""

from typing import List


def chunk_text(text: str, max_length: int = 500, overlap: int = 50) -> List[str]:
    if not text:
        return []

    chunks = []
    start = 0
    text = text.strip()

    while start < len(text):
        end = start + max_length
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
