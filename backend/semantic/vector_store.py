# backend/semantic/vector_store.py
import numpy as np
from sqlalchemy import text
from backend.db import get_db_session

def search_employees(query_vector: list, top_k: int = 5):
    """
    Perform a semantic search in the employees table using pgvector.
    """
    session = get_db_session()
    try:
        sql = text("""
        SELECT id, name, department_id, salary
        FROM employees
        ORDER BY employees_embedding <-> :vec
        LIMIT :top_k
        """)
        result = session.execute(sql, {"vec": query_vector, "top_k": top_k})
        return result.fetchall()
    finally:
        session.close()
