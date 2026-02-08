import os
from typing import List, Dict
import markdown

def _clean_markdown(md_text: str) -> str:
    """
    Convert markdown text to plain text.
    """
    html = markdown.markdown(md_text)
    # Very lightweight HTML tag removal
    text = (
        html.replace("<p>", "")
        .replace("</p>", "\n")
        .replace("<br />", "\n")
    )
    return text

def chunk_markdown_file(
    file_path: str,
    max_chars: int = 800
) -> List[Dict[str, str]]:
    """
    Reads a markdown file and splits it into text chunks.

    Returns a list of dictionaries:
    {
        "text": chunk_text,
        "source": filename
    }
    """
    if not file_path.endswith(".md"):
        raise ValueError("Only markdown (.md) files are supported")

    with open(file_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    plain_text = _clean_markdown(raw_md)
    paragraphs = [p.strip() for p in plain_text.split("\n") if p.strip()]

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) <= max_chars:
            current_chunk += " " + para
        else:
            chunks.append({
                "text": current_chunk.strip(),
                "source": os.path.basename(file_path)
            })
            current_chunk = para

    if current_chunk.strip():
        chunks.append({
            "text": current_chunk.strip(),
            "source": os.path.basename(file_path)
        })

    return chunks
