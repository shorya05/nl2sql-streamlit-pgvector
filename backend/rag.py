# backend/rag.py

def generate_rag_answer(query: str, k_each: int = 5):
    """
    Fake RAG answer generator (no OpenAI required).
    Returns a placeholder answer and some mock retrieved documents.
    """

    # Simple dummy answer
    answer = f"(Mock Answer) Based on your query: '{query}', here are some relevant results."

    # Pretend we retrieved documents from pgvector
    meta = {
        "products": [
            {"id": 1, "name": "Laptop", "price": 1200.00},
            {"id": 2, "name": "Phone", "price": 800.00},
        ],
        "orders": [
            {"id": 101, "customer_name": "Alice", "order_total": 300.00},
            {"id": 102, "customer_name": "Bob", "order_total": 450.00},
        ],
        "employees": [
            {"id": 5, "name": "Eve", "department_id": 2},
            {"id": 6, "name": "Charlie", "department_id": 1},
        ],
    }

    return {
        "answer": answer,
        "meta": meta
    }
