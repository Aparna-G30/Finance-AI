import sqlite3
def get_connection():
    conn=sqlite3.connect("finance.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        merchant TEXT,
        amount REAL,
        date TEXT,
        category TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        category TEXT PRIMARY KEY,
        budget REAL
    )
    """)

    conn.commit()
    conn.close()  
