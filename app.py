# app.py
import streamlit as st
import pandas as pd

# App title
st.set_page_config(page_title="Data Dashboard", page_icon="📊", layout="wide")
st.title("📊 Interactive Data Dashboard")

# Sidebar
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    # Show raw data
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # Show basic info
    st.subheader("📈 Dataset Overview")
    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    st.write("**Summary Statistics:**")
    st.write(df.describe())

    # Column selection for charts
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        st.subheader("📊 Visualizations")

        # Histogram
        col = st.selectbox("Choose a column for Histogram", numeric_cols)
        st.bar_chart(df[col].value_counts())

        # Scatter plot
        st.subheader("Scatter Plot")
        x_axis = st.selectbox("X-axis", numeric_cols, index=0)
        y_axis = st.selectbox("Y-axis", numeric_cols, index=min(1, len(numeric_cols)-1))
        st.scatter_chart(df[[x_axis, y_axis]])
    else:
        st.warning("No numeric columns available for visualization.")

    # Download button
    st.subheader("💾 Download Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download CSV",
        csv,
        "processed_data.csv",
        "text/csv",
        key="download-csv"
    )
else:
    st.info("👈 Please upload a CSV file to start.")

