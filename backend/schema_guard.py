import re

def validate_select(sql: str):
    """
    Only allow safe SELECT statements.
    """
    s = sql.strip().lower()
    if not s.startswith("select"):
        raise ValueError("Only SELECT queries allowed")
    forbidden = ["insert", "update", "delete", "drop", "alter", "create"]
    for f in forbidden:
        if f in s:
            raise ValueError(f"Forbidden SQL keyword: {f}")
    return True
