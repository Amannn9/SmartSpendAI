import streamlit as st
import sys

st.title("Debug Environment")

st.write("Python Version:", sys.version)

try:
    import plotly
    st.success(f"Plotly Installed: {plotly.__version__}")
except Exception as e:
    st.error(f"Plotly Error: {e}")

try:
    import reportlab
    st.success(f"ReportLab Installed: {reportlab.Version}")
except Exception as e:
    st.error(f"ReportLab Error: {e}")

try:
    import sklearn
    st.success(f"Scikit-Learn Installed: {sklearn.__version__}")
except Exception as e:
    st.error(f"Scikit-Learn Error: {e}")