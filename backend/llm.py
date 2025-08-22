from sqlalchemy import text
from backend.db import get_db_session

# Example function: Convert simple NL query → SQL
def generate_sql(nl_query: str):
    query = nl_query.lower()
    if "top 5 employees by salary" in query:
        return """
            SELECT id, name, department_id, email, salary
            FROM employees
            ORDER BY salary DESC
            LIMIT 5
        """
    elif "sales" in query and "most" in query:
        return """
            SELECT id, name, department_id, email, salary
            FROM employees
            WHERE department_id = 2
            ORDER BY salary DESC
            LIMIT 1
        """
    elif "engineering" in query and "salary > 65000" in query:
        return """
            SELECT id, name, department_id, email, salary
            FROM employees
            WHERE department_id = 1 AND salary > 65000
        """
    elif "hr" in query and "email" in query:
        return """
            SELECT email FROM employees WHERE department_id = 3
        """
    elif "departments" in query:
        return "SELECT * FROM departments"
    else:
        # fallback
        return None

# Execute SQL safely
def execute_sql(sql):
    if not sql:
        return []
    session = get_db_session()
    try:
        result = session.execute(text(sql)).fetchall()
        return result
    finally:
        session.close()
