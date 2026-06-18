import sqlite3
import streamlit as st
import os


def get_db_name():

    user_code = st.session_state.get(
        "user_code",
        "guest"
    )

    return f"data/{user_code}.db"


def create_database():

    os.makedirs(
        "data",
        exist_ok=True
    )

    db_name = get_db_name()

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        expense_date TEXT NOT NULL
    )
    """)

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