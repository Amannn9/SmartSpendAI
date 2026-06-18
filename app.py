import streamlit as st
from utils.database import create_database

st.set_page_config(
    page_title="SmartSpend AI",
    page_icon="💰",
    layout="wide"
)

# User Access Code System
if "user_code" not in st.session_state:

    st.title("💰 SmartSpend AI")

    st.subheader("Enter Your Access Code")

    user_code = st.text_input(
        "Access Code",
        placeholder="Example: Aman, Rahul, Guest1"
    )

    if st.button("Continue"):

        if user_code.strip():

            st.session_state.user_code = user_code.strip()

            st.rerun()

        else:

            st.warning("Please enter an access code.")

    st.stop()

# Create user-specific database
create_database()

# Sidebar
with st.sidebar:

    st.success(
        f"Logged in as: {st.session_state.user_code}"
    )

    if st.button("Logout"):

        del st.session_state.user_code

        st.rerun()

# Home Page
st.title("💰 SmartSpend AI")

st.success("Database Connected Successfully")

st.write(
    """
    Welcome to SmartSpend AI.

    Features:
    - Expense Tracking
    - Budget Management
    - Savings Analysis
    - Expense Prediction
    - PDF Export Reports
    """
)