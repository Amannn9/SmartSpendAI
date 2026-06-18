import streamlit as st
import sqlite3
import pandas as pd

from utils.database import (
    create_database,
    get_db_name
)

from ml.expense_predictor import (
    predict_next_expense
)

create_database()

DB_NAME = get_db_name()

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

    st.dataframe(
        expenses_df,
        use_container_width=True
    )