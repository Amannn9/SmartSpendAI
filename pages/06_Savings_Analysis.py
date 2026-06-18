import streamlit as st
import sqlite3
import pandas as pd

from utils.database import (
    create_database,
    get_db_name
)

create_database()

DB_NAME = get_db_name()

st.title("🏦 Savings Analysis")

conn = sqlite3.connect(DB_NAME)

expenses_df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

budget_df = pd.read_sql_query(
    "SELECT * FROM monthly_budget",
    conn
)

conn.close()

if budget_df.empty:

    st.warning(
        "Please add a budget first."
    )

else:

    income = budget_df.iloc[-1]["income"]

    savings_goal = budget_df.iloc[-1]["savings_goal"]

    total_expense = (
        expenses_df["amount"].sum()
        if not expenses_df.empty
        else 0
    )

    actual_savings = (
        income - total_expense
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Actual Savings",
        f"₹{actual_savings:,.0f}"
    )

    col2.metric(
        "Savings Goal",
        f"₹{savings_goal:,.0f}"
    )

    if actual_savings >= savings_goal:

        st.success(
            "🎉 Congratulations! You achieved your savings goal."
        )

    else:

        shortfall = (
            savings_goal - actual_savings
        )

        st.error(
            f"⚠️ You are ₹{shortfall:,.0f} away from your goal."
        )