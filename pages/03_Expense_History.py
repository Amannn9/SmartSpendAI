import streamlit as st
import sqlite3
import pandas as pd

from utils.database import (
    create_database,
    get_db_name
)

create_database()

DB_NAME = get_db_name()

st.title("📋 Expense History")

conn = sqlite3.connect(DB_NAME)

df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

conn.close()

if df.empty:
    st.warning("No expenses found.")
    st.stop()

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

st.subheader("🗑 Delete Expense")

expense_id = st.selectbox(
    "Select Expense ID",
    df["id"].tolist()
)

if st.button("Delete Expense"):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (int(expense_id),)
    )

    conn.commit()
    conn.close()

    st.success(
        "Expense deleted successfully ✅"
    )

    st.rerun()