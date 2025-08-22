# backend/hybrid_search.py
from backend.db import engine
from sqlalchemy import text

# ---- Product semantic search
def vector_search_products(query: str, k: int = 10):
    with engine.begin() as conn:
        rows = conn.execute(
            text("""
            SELECT id, name, price
            FROM products
            ORDER BY random()
            LIMIT :k
            """), {"k": k}
        )
        return [dict(r) for r in rows]

# ---- Customer / orders semantic search
def vector_search_customers(query: str, k: int = 10):
    with engine.begin() as conn:
        rows = conn.execute(
            text("""
            SELECT id, customer_name, order_total, order_date
            FROM orders
            ORDER BY random()
            LIMIT :k
            """), {"k": k}
        )
        return [dict(r) for r in rows]

# ---- Hybrid routing (decide which search path to use)
def hybrid_route(query: str):
    q = query.lower()
    if "product" in q:
        return "products"
    elif "customer" in q or "order" in q:
        return "customers"
    else:
        return "sql"
