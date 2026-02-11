# Smart Notes – Local Q&A (RAG MVP)

This is a minimal, local-first MVP that allows users to ask natural-language questions over their markdown notes.

## Features (Current MVP)

- Loads markdown files from a local `notes/` directory
- Supports natural-language questions (e.g., "what is AI", "where is AI used")
- Returns sentence-level answers from notes
- Shows the source note filename
- Interactive CLI loop (type `exit` to quit)

This is a starter implementation intended to be extended with embeddings and vector search in future iterations.

---

## How it works

1. Notes are loaded from the local `notes/` directory.
2. Question words (what, where, who, when, etc.) are filtered.
3. Notes are split into sentences.
4. Relevant sentences are returned based on keyword matching.

---

## How to run

```bash
python smart-notes/rag_mvp/qa_cli.py



>> what is AI

[1] From test.md:
Artificial Intelligence (AI) is the simulation of human intelligence in machines.


>>  what is machine learning
how is machine learning used
difference between AI and ML





# Smart Notes – RAG MVP (Embeddings & FAISS)

This project is a simple **Retrieval-Augmented Generation (RAG)** pipeline for Smart Notes.  
It allows users to store notes, convert them into embeddings, and search relevant notes using vector similarity.

---

## 🚀 Features

- Convert notes into embeddings using Sentence Transformers
- Store and search embeddings using FAISS (CPU)
- CLI tool to ask questions about your notes
- Simple chunking for text files
- Works fully offline after model download

---

## 🧠 Tech Stack

- Python 3.10+
- sentence-transformers  
- FAISS (faiss-cpu)  
- HuggingFace Transformers

---

## 📁 Project Structure

```bash
smart-notes/
├── rag_mvp/
│   ├── embed.py        # Embedding logic
│   ├── index.py        # FAISS index creation
│   ├── qa_cli.py       # CLI for asking questions
│   └── utils.py        # Helper functions
├── notes/              # Put your .txt notes here
├── requirements.txt
└── README.md
