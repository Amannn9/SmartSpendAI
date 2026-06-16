import sqlite3

DB_NAME = "data/expenses.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Expenses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        expense_date TEXT NOT NULL
    )
    """)

    # Budget table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS monthly_budget(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        income REAL NOT NULL,
        savings_goal REAL NOT NULL,
        month TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()