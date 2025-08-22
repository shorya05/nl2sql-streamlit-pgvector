from backend.semantic.query import semantic_employee_search

query = "top paid employees in tech"
results = semantic_employee_search(query, top_k=5)

for r in results:
    print(r)
