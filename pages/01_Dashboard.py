import streamlit as st

# Debug Plotly Import
try:
    import plotly.express as px
except Exception as e:
    st.error(f"Plotly Import Error: {e}")
    st.stop()

import sqlite3
import pandas as pd

from utils.database import create_database

DB_NAME = "data/expenses.db"

st.title("📊 Dashboard")

# Create database if not exists
create_database()

# Database Connection
conn = sqlite3.connect(DB_NAME)

try:
    expenses_df = pd.read_sql_query(
        "SELECT * FROM expenses",
        conn
    )
except Exception as e:
    st.error(f"Error loading expenses: {e}")
    expenses_df = pd.DataFrame()

try:
    budget_df = pd.read_sql_query(
        "SELECT * FROM monthly_budget",
        conn
    )
except Exception as e:
    st.error(f"Error loading budget: {e}")
    budget_df = pd.DataFrame()

conn.close()

# Metrics
total_expense = (
    expenses_df["amount"].sum()
    if not expenses_df.empty
    else 0
)

income = (
    budget_df["income"].sum()
    if not budget_df.empty
    else 0
)

savings = income - total_expense

savings_goal = (
    budget_df.iloc[-1]["savings_goal"]
    if not budget_df.empty
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Income", f"₹{income:,.0f}")
col2.metric("💸 Expenses", f"₹{total_expense:,.0f}")
col3.metric("🏦 Savings", f"₹{savings:,.0f}")
col4.metric("🎯 Savings Goal", f"₹{savings_goal:,.0f}")

# ----------------------------------------------------
# Expense Distribution Pie Chart
# ----------------------------------------------------

st.divider()

st.subheader("🥧 Expense Distribution")

if not expenses_df.empty:

    category_expense = (
        expenses_df.groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    pie_fig = px.pie(
        category_expense,
        names="category",
        values="amount",
        hole=0.4,
        title="Expenses by Category"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

else:
    st.info("Add expenses to view analytics.")

# ----------------------------------------------------
# Category Wise Spending
# ----------------------------------------------------

st.divider()

st.subheader("📊 Category Wise Spending")

if not expenses_df.empty:

    category_expense = (
        expenses_df.groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    bar_fig = px.bar(
        category_expense,
        x="category",
        y="amount",
        text_auto=True,
        title="Category Wise Expenses"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

# ----------------------------------------------------
# Monthly Expense Trend
# ----------------------------------------------------

st.divider()

st.subheader("📈 Monthly Expense Trend")

if not expenses_df.empty:

    expenses_df["expense_date"] = pd.to_datetime(
        expenses_df["expense_date"]
    )

    monthly_expense = (
        expenses_df.groupby(
            expenses_df["expense_date"].dt.to_period("M")
        )["amount"]
        .sum()
        .reset_index()
    )

    monthly_expense["expense_date"] = (
        monthly_expense["expense_date"]
        .astype(str)
    )

    line_fig = px.line(
        monthly_expense,
        x="expense_date",
        y="amount",
        markers=True,
        title="Monthly Spending Trend"
    )

    st.plotly_chart(
        line_fig,
        use_container_width=True
    )

# ----------------------------------------------------
# Income vs Expense
# ----------------------------------------------------

st.divider()

st.subheader("💰 Budget vs Expenses")

if not budget_df.empty:

    latest_income = (
        budget_df.iloc[-1]["income"]
    )

    compare_df = pd.DataFrame({
        "Type": ["Income", "Expenses"],
        "Amount": [latest_income, total_expense]
    })

    compare_fig = px.bar(
        compare_df,
        x="Type",
        y="Amount",
        text_auto=True,
        title="Income vs Expenses"
    )

    st.plotly_chart(
        compare_fig,
        use_container_width=True
    )

else:
    st.info("Set a budget to compare income and expenses.")