# # backend/seed.py
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# import numpy as np
# from sqlalchemy.orm import Session
# from backend.db import get_db_session

# def seed_employees(num=10):
#     session: Session = get_db_session()
#     try:
#         for i in range(1, num + 1):
#             vector = list(np.random.rand(1536))
#             session.execute(
#                 """
#                 UPDATE employees
#                 SET name_embedding = :vec
#                 WHERE id = :id
#                 """,
#                 {"vec": vector, "id": i}
#             )
#         session.commit()
#     finally:
#         session.close()

# if __name__ == "__main__":
#     seed_employees()
#     print("Employees seeded with random embeddings!")
# backend/seed.py
import numpy as np
from sqlalchemy import text
from backend.db import get_db_session

def seed_employees(num=10):
    session = get_db_session()
    try:
        for i in range(1, num + 1):
            # Convert to plain Python floats
            vector = [float(x) for x in np.random.rand(1536)]
            
            # For pgvector column, just pass the Python list
            sql = text("""
                UPDATE employees
                SET name_embedding = :vec
                WHERE id = :id
            """)
            
            session.execute(sql, {"vec": vector, "id": i})
        session.commit()
    finally:
        session.close()

if __name__ == "__main__":
    seed_employees()
    print("Employees seeded with random embeddings!")
