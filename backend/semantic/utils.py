# backend/semantic/utils.py
from sentence_transformers import SentenceTransformer

# Load a local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # small, fast, good quality

def text_to_embedding(text: str) -> list:
    """
    Convert text to embedding vector using a local model.
    """
    embedding = model.encode(text)
    return embedding.tolist()  # convert numpy array to list
