# backend/query.py
from backend.db import get_db_session
from sqlalchemy import text

def query_top_employees_by_salary(limit=5):
    session = get_db_session()
    try:
        sql = text("""
            SELECT id, name, department_id, email, salary
            FROM employees
            ORDER BY salary DESC
            LIMIT :limit
        """)
        result = session.execute(sql, {"limit": limit}).fetchall()
        return result
    finally:
        session.close()
