# backend/semantic/query.py
from backend.semantic.vector_store import search_employees
from backend.semantic.utils import text_to_embedding

def semantic_employee_search(query_text: str, top_k: int = 5):
    """
    Convert NL query to embedding and perform semantic search.
    """
    query_vector = text_to_embedding(query_text)
    results = search_employees(query_vector, top_k)
    
    return results
