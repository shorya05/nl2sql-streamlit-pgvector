# backend/semantic/embeddings_cache.py
import hashlib

CACHE = {}

def cache_embedding(text: str, embedding: list):
    key = hashlib.sha256(text.encode()).hexdigest()
    CACHE[key] = embedding

def get_cached_embedding(text: str):
    key = hashlib.sha256(text.encode()).hexdigest()
    return CACHE.get(key, None)
