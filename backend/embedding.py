from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

def embed_one(text: str):
    """Return a vector embedding for text."""
    if not text:
        return None
    res = client.embeddings.create(model=EMBED_MODEL, input=text)
    return res.data[0].embedding
