import psycopg2
conn = psycopg2.connect(
    dbname="nl2sql",
    user="postgres",
    password="Shorya@123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("SELECT * FROM employees;")
print(cur.fetchall())
cur.close()
conn.close()
