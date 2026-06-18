import streamlit as st
import sqlite3
import pandas as pd

from utils.database import (
    create_database,
    get_db_name
)

create_database()

DB_NAME = get_db_name()

st.title("✏️ Edit Expense")

conn = sqlite3.connect(DB_NAME)

df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

conn.close()

if df.empty:
    st.warning("No expenses found.")
    st.stop()

expense_id = st.selectbox(
    "Select Expense ID",
    df["id"].tolist()
)

selected = df[
    df["id"] == expense_id
].iloc[0]

amount = st.number_input(
    "Amount",
    value=float(selected["amount"])
)

category = st.text_input(
    "Category",
    value=selected["category"]
)

description = st.text_input(
    "Description",
    value=str(selected["description"])
)

expense_date = st.text_input(
    "Expense Date",
    value=str(selected["expense_date"])
)

if st.button("Update Expense"):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE expenses
    SET amount=?,
        category=?,
        description=?,
        expense_date=?
    WHERE id=?
    """,
    (
        amount,
        category,
        description,
        expense_date,
        expense_id
    ))

    conn.commit()
    conn.close()

    st.success(
        "Expense updated successfully ✅"
    )

    st.rerun()