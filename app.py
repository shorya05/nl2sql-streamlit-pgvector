# import streamlit as st
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# # Database setup
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5433/company"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db_session():
#     return SessionLocal()

# # Streamlit UI
# st.title("💼 Natural Language SQL + pgvector Demo")
# st.write("Ask a question about employees, departments, or orders:")

# query = st.text_input("Type your question here:")

# if st.button("Run Query") and query:
#     session = get_db_session()
#     try:
#         sql = None
#         q_lower = query.lower()

#         # Employee-focused queries
#         if "top" in q_lower and "salary" in q_lower:
#             sql = text("SELECT id, name, department_id, email, salary FROM employees ORDER BY salary DESC LIMIT 5")
#         elif "sales" in q_lower and "most" in q_lower:
#             sql = text("SELECT id, name, department_id, email, salary FROM employees WHERE department_id=2 ORDER BY salary DESC LIMIT 5")
#         elif "engineering" in q_lower and "salary" in q_lower:
#             sql = text("SELECT id, name, department_id, email, salary FROM employees WHERE department_id=1 AND salary>65000")
#         elif "hr" in q_lower and "email" in q_lower:
#             sql = text("SELECT name, email FROM employees WHERE department_id=3")
#         elif "department 2" in q_lower:
#             sql = text("SELECT * FROM employees WHERE department_id=2")
#         elif "starts with 'c'" in q_lower:
#             sql = text("SELECT * FROM employees WHERE name ILIKE 'C%'")
#         elif "compare salaries" in q_lower:
#             sql = text("SELECT department_id, AVG(salary) as avg_salary FROM employees GROUP BY department_id")

#         # Department-focused queries
#         elif "all departments" in q_lower:
#             sql = text("SELECT * FROM departments")
#         elif "how many employees" in q_lower:
#             sql = text("SELECT department_id, COUNT(*) as employee_count FROM employees GROUP BY department_id")
#         elif "average salary" in q_lower:
#             sql = text("SELECT department_id, AVG(salary) as avg_salary FROM employees GROUP BY department_id")
#         elif "highest-paid employee" in q_lower:
#             sql = text("SELECT * FROM employees ORDER BY salary DESC LIMIT 1")

#         # Orders / Customers (example, if tables exist)
#         elif "orders over" in q_lower:
#             sql = text("SELECT * FROM orders WHERE order_total > 400")
#         elif "most orders" in q_lower:
#             sql = text("SELECT customer_name, COUNT(*) as order_count FROM orders GROUP BY customer_name ORDER BY order_count DESC LIMIT 1")
#         elif "total sales" in q_lower:
#             sql = text("SELECT customer_name, SUM(order_total) as total_sales FROM orders GROUP BY customer_name")
#         elif "top products" in q_lower:
#             sql = text("SELECT * FROM products ORDER BY price DESC LIMIT 5")

#         # Execute mapped query
#         if sql is not None:
#             results = session.execute(sql).fetchall()
#             if results:
#                 for r in results:
#                     st.write(dict(r._mapping))
#             else:
#                 st.info("No results found.")
#         else:
#             st.warning("Query not recognized. Try one of the predefined queries or expand the mapping.")

#     finally:
#         session.close()

# app.py
# app.py
import streamlit as st
from backend.llm import generate_sql, execute_sql

st.title("🧭 NL2SQL + pgvector Demo")
st.write("Ask a question about employees, departments, or orders:")

query = st.text_input("Enter your natural language query:")

if st.button("Submit") and query:
    st.info("🔎 Generating SQL...")
    sql = generate_sql(query)
    
    if sql:
        st.code(sql, language="sql")
        st.info("📊 Executing SQL...")
        try:
            results = execute_sql(sql)
            if results:
                st.table(results)
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"Error executing SQL: {e}")
    else:
        st.warning("❌ Could not generate SQL for this query. Try another query.")

# # Example queries
# st.markdown("""
# 💡 Tips / Examples:

# - Show top 5 employees by salary  
# - Who earns the most in Sales?  
# - List employees in Engineering with salary > 65000  
# - Get email addresses of all HR employees  
# - List all departments
# """)
