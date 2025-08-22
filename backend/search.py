from backend.db import engine
from backend.embedding import embed_one
from sqlalchemy import text

def vector_search_products(query: str, k=5):
    v = embed_one(query)
    sql = text("""
        SELECT id, name, price, 1 - (name_embedding <=> :v) AS similarity
        FROM products
        ORDER BY name_embedding <=> :v
        LIMIT :k
    """)
    with engine.begin() as conn:
        return conn.execute(sql, {"v": v, "k": k}).mappings().all()

def vector_search_customers(query: str, k=5):
    v = embed_one(query)
    sql = text("""
        SELECT id, customer_name, order_total, order_date,
               1 - (customer_name_embedding <=> :v) AS similarity
        FROM orders
        ORDER BY customer_name_embedding <=> :v
        LIMIT :k
    """)
    with engine.begin() as conn:
        return conn.execute(sql, {"v": v, "k": k}).mappings().all()
