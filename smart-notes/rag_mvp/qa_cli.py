import os
import re

#-------------------emedding-pipeline-chunking concept
from rag_mvp.pipelines.embedding_pipeline import EmbeddingPipeline

def demo_embeddings_pipeline():
    pipeline = EmbeddingPipeline()

    note_text = """
    Python is a programming language.
    It is widely used in AI and machine learning projects.
    Smart Notes helps users organize knowledge using embeddings.
    """

    chunks, embeddings = pipeline.process_notes(note_text)

    print("\n--- Chunks Created ---")
    for i, c in enumerate(chunks):
        print(f"[{i}] {c}")

    query = "What is Python used for?"
    results = pipeline.semantic_search(query)

    print("\n--- Search Results ---")
    for r in results:
        print("-", r)
#-------------------------------------------------




QUESTION_WORDS = {
    "what", "where", "who", "when", "which",
    "is", "are", "was", "were", "the", "a", "an",
    "of", "to", "in", "on", "for"
}

NOTES_DIR = "notes"


def load_notes():
    notes = []
    if not os.path.exists(NOTES_DIR):
        print(f"Notes directory '{NOTES_DIR}' not found.")
        return notes

    for file in os.listdir(NOTES_DIR):
        if file.endswith(".md"):
            path = os.path.join(NOTES_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                notes.append({
                    "filename": file,
                    "content": f.read()
                })
    return notes


def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)


def search_notes(query, notes):
    results = []

    query_words = [
        word.lower()
        for word in query.split()
        if word.lower() not in QUESTION_WORDS
    ]

    for note in notes:
        sentences = split_sentences(note["content"])
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(word in sentence_lower for word in query_words):
                results.append({
                    "filename": note["filename"],
                    "sentence": sentence.strip()
                })

    return results


if __name__ == "__main__":

    demo_embeddings_pipeline()      # Temporary demo for embeddings pipeline

    notes = load_notes()

    print("Ask questions about your notes (type 'exit' to quit)\n")

    while True:
        query = input(">> ").strip()

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        matches = search_notes(query, notes)

        if not matches:
            print("No relevant notes found.\n")
        else:
            print("\n--- Answers ---\n")
            for i, m in enumerate(matches, 1):
                print(f"[{i}] From {m['filename']}:")
                print(m["sentence"])
                print()
