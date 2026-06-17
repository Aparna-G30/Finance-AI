from db import get_connection

def add_expenses(merchant,amount,date,category):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    INSERT INTO expenses(merchant,amount,date,category)
    VALUES(?,?,?,?)
    """,(merchant,amount,date,category))

    conn.commit()
    conn.close()

def get_all_expenses():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows=cursor.fetchall()

    conn.close()
    return rows

def delete_expenses(expense_id):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?",(expense_id,))

    conn.commit()
    conn.close()

def update_expenses(expense_id,merchant,amount,date,category):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    UPDATE expenses
    SET merchant=?,amount=?,date=?,category=?
    WHERE id=?
     """,(merchant,amount,date,category,expense_id))
    
    conn.commit()
    conn.close()

def get_expense_by_category(category):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    WHERE category=? """,(category,))
    
    rows=cursor.fetchall()
    conn.close()
    return rows

def get_expense_by_merchant(merchant):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    WHERE merchant=? """,(merchant,))
    
    rows=cursor.fetchall()
    conn.close()
    return rows

def get_sorted_by_amount():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    ORDER BY amount DESC 
    """)

    rows=cursor.fetchall()
    conn.close()
    return rows

def get_total_spending():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses""")

    total=cursor.fetchone()[0]
    conn.close()
    return total

def get_category_totals():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    cat_total=cursor.fetchall()
    conn.close()
    return cat_total

def get_monthly_expenses():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT substr(date,1,7) AS month,
                   SUM(amount)
    FROM expenses
    GROUP BY month""")

    month_total=cursor.fetchall()
    conn.close()
    return month_total

def get_monthly_report(month_rep):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT *
    FROM expenses
    WHERE substr(date,1,7)=?
    """,(month_rep,))

    monthly_expenses=cursor.fetchall()
    conn.close()
    return monthly_expenses

def get_sorted_by_merchant():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    ORDER BY merchant
    """)

    rows=cursor.fetchall()
    conn.close()
    return rows

def get_sorted_by_date():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    ORDER BY date DESC 
    """)

    rows=cursor.fetchall()
    conn.close()
    return rows

def get_highest_expense_monthly(month_rep):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT merchant, amount
    FROM expenses
    WHERE substr(date,1,7)=?
    ORDER BY amount DESC
    LIMIT 1
    """, (month_rep,))

    row = cursor.fetchone()

    conn.close()
    return row

def get_lowest_expense_monthly(month_rep):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT merchant, amount
    FROM expenses
    WHERE substr(date,1,7)=?
    ORDER BY amount ASC
    LIMIT 1
    """, (month_rep,))

    row = cursor.fetchone()

    conn.close()
    return row

def get_highest_expense():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT merchant, amount
    FROM expenses
    ORDER BY amount DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()
    return row

def get_lowest_expense():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT merchant, amount
    FROM expenses
    ORDER BY amount ASC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()
    return row