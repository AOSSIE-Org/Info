import os
import sys
from typing import List

from semantic_search.chunker import chunk_markdown_file
from semantic_search.embedder import Embedder
from semantic_search.vector_store import VectorStore

def load_markdown_files(folder_path: str) -> List[str]:
    files = []
    for fname in os.listdir(folder_path):
        if fname.endswith(".md"):
            files.append(os.path.join(folder_path, fname))
    return files


def main():
    if len(sys.argv) < 3:
        print("Usage: python search.py <notes_folder> <query>")
        sys.exit(1)

    notes_folder = sys.argv[1]
    query = sys.argv[2]

    markdown_files = load_markdown_files(notes_folder)
    if not markdown_files:
        print("No markdown files found.")
        sys.exit(1)

    all_chunks = []
    for md_file in markdown_files:
        all_chunks.extend(chunk_markdown_file(md_file))

    texts = [c["text"] for c in all_chunks]

    embedder = Embedder()
    embeddings = embedder.embed_texts(texts)

    vector_store = VectorStore(embedding_dim=len(embeddings[0]))
    vector_store.add(embeddings, all_chunks)

    query_embedding = embedder.embed_texts([query])[0]
    results = vector_store.search(query_embedding, k=5)

    print("\nTop results:\n")
    for res in results:
        print(f"- {res['source']} (score: {res['score']:.3f})")
        print(f"  {res['text'][:200]}...\n")


if __name__ == "__main__":
    main()
