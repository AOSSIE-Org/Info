# Local Semantic Search MVP

This module implements a minimal, local-first semantic search pipeline for markdown notes.
It is designed as a foundational building block for the Smart Notes GSoC 2026 idea.

## Features
- Markdown file ingestion
- Automatic text chunking
- Local embeddings using Sentence Transformers (MiniLM)
- Vector similarity search using FAISS
- Fully offline after initial model download

## Usage

From the repository root:

```bash
python -m semantic_search.search semantic_search/test_notes "your query here"
