# import streamlit as st

# st.set_page_config(
#     page_title="SmartSpend AI",
#     page_icon="💰",
#     layout="wide"
# )

# st.title("💰 SmartSpend AI")

# st.write("Welcome to your AI-powered Expense Tracker")

import streamlit as st
from utils.database import create_database

create_database()

st.set_page_config(
    page_title="SmartSpend AI",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SmartSpend AI")

st.success("Database Connected Successfully")