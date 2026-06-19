from backend.db import get_connection

def set_budget(category,budget):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    INSERT INTO budgets(category,budget)
    VALUES(?,?)
    """,(category,budget))

    conn.commit()
    conn.close()

def get_budget():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM budgets")

    rows=cursor.fetchall()
    conn.close()
    return rows

def check_budget():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT 
        expenses.category,
        SUM(expenses.amount),
        budgets.budget
    FROM expenses
    JOIN budgets
    ON expenses.category=budgets.category
    GROUP BY expense.category
    """)
    
    results=cursor.fetchall()
    conn.close()
    return results