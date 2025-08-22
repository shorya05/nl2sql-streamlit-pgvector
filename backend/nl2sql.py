# backend/nl2sql.py

def to_sql(query: str):
    """
    Fake NL→SQL translator (no OpenAI required).
    Returns simple SQL templates based on keywords.
    """
    q = query.lower()
    params = {}

    if "department" in q:
        sql = """
        SELECT d.name, COUNT(e.id) AS num_employees
        FROM departments d
        LEFT JOIN employees e ON d.id = e.department_id
        GROUP BY d.name;
        """
    elif "orders" in q:
        sql = """
        SELECT customer_name, order_total, order_date
        FROM orders
        ORDER BY order_date DESC
        LIMIT 10;
        """
    elif "products" in q:
        sql = "SELECT id, name, price FROM products LIMIT 10;"
    else:
        sql = "SELECT * FROM employees LIMIT 10;"

    return sql.strip(), params
