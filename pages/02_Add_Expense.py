import streamlit as st
import sqlite3
from datetime import date

from utils.database import (
    create_database,
    get_db_name
)

create_database()

DB_NAME = get_db_name()

st.title("➕ Add Expense")

amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=1.0
)

category = st.selectbox(
    "Category",
    [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Education",
        "Bills",
        "Others"
    ]
)

description = st.text_input("Description")

expense_date = st.date_input(
    "Expense Date",
    value=date.today()
)

if st.button("Save Expense"):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses
    (
        amount,
        category,
        description,
        expense_date
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        amount,
        category,
        description,
        str(expense_date)
    ))

    conn.commit()
    conn.close()

    st.success("Expense Added Successfully ✅")