import streamlit as st
import sqlite3
import pandas as pd
from utils.pdf_generator import generate_pdf


DB_NAME = "data/expenses.db"

st.title("📥 Export Reports")

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

income = (
    budget_df.iloc[-1]["income"]
    if not budget_df.empty
    else 0
)

savings_goal = (
    budget_df.iloc[-1]["savings_goal"]
    if not budget_df.empty
    else 0
)

total_expenses = (
    expenses_df["amount"].sum()
    if not expenses_df.empty
    else 0
)

savings = income - total_expenses

st.subheader("Expense Records")

st.dataframe(
    expenses_df,
    use_container_width=True
)

# Export Expenses CSV

expense_csv = expenses_df.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Expenses CSV",
    data=expense_csv,
    file_name="expenses_report.csv",
    mime="text/csv"
)

# Export Budget CSV

budget_csv = budget_df.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Budget CSV",
    data=budget_csv,
    file_name="budget_report.csv",
    mime="text/csv"
)



if st.button("Generate PDF Report"):

    generate_pdf(
        "SmartSpend_Report.pdf",
        income,
        total_expenses,
        savings,
        savings_goal
    )

    with open(
        "SmartSpend_Report.pdf",
        "rb"
    ) as file:
        
        pdf_bytes = file.read()

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_bytes,
            file_name="SmartSpend_Report.pdf",
            mime="application/pdf"
        )