import streamlit as st
import sqlite3
import pandas as pd

from ml.expense_predictor import (
    predict_next_expense
)

DB_NAME = "data/expenses.db"

st.title("🤖 AI Expense Prediction")

conn = sqlite3.connect(DB_NAME)

expenses_df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

conn.close()

prediction = predict_next_expense(
    expenses_df
)

if prediction is None:

    st.warning(
        "Add at least 3 expense records for prediction."
    )

else:

    st.metric(
        "Predicted Next Expense",
        f"₹{prediction:,.2f}"
    )

    st.success(
        "Prediction generated using Linear Regression."
    )