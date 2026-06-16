import streamlit as st
import sqlite3
import pandas as pd

from ml.expense_predictor import predict_next_expense

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
        "Add expense records from at least 3 different months for prediction."
    )

else:

    st.metric(
        "Predicted Next Month Expense",
        f"₹{prediction:,.2f}"
    )

    st.success(
        "Prediction generated using Linear Regression."
    )

    st.subheader("Historical Expense Data")

    st.dataframe(
        expenses_df,
        use_container_width=True
    )