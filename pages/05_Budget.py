import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "data/expenses.db"

st.title("💵 Monthly Budget")

income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    step=100.0
)

savings_goal = st.number_input(
    "Savings Goal",
    min_value=0.0,
    step=100.0
)

month = st.text_input(
    "Month",
    value=datetime.now().strftime("%B %Y")
)

if st.button("Save Budget"):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO monthly_budget
    (income, savings_goal, month)
    VALUES (?, ?, ?)
    """,
    (
        income,
        savings_goal,
        month
    ))

    conn.commit()
    conn.close()

    st.success("Budget Saved Successfully ✅")


st.divider()

st.subheader("Saved Budgets")

conn = sqlite3.connect(DB_NAME)

budget_df = pd.read_sql_query(
    """
    SELECT *
    FROM monthly_budget
    ORDER BY id DESC
    """,
    conn
)

conn.close()

st.dataframe(
    budget_df,
    use_container_width=True
)