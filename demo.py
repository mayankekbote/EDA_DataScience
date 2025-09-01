import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.title("📊 EDA Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File loaded successfully!")

    # Option to view dataset
    if st.checkbox("View Uploaded CSV"):
        st.dataframe(df.head(50))  # show first 50 rows

    # Create tabs for different EDA steps
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Missing Values & Info", "Summary Statistics", "Distributions", "Correlation", "Categorical Analysis"]
    )

    # 1. Missing values & data types
    with tab1:
        st.subheader("📌 Missing Values & Data Types")

        info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values,
        "Non-Null Count": df.notnull().sum().values,
        "Missing Count": df.isnull().sum().values
        })
        st.write("### Missing Values")
        st.write(df.isnull().sum())

    # 2. Summary statistics
    with tab2:
        st.subheader("📌 Summary Statistics")
        st.write(df.describe(include="all"))

    # 3. Distribution plots
    with tab3:
        st.subheader("📌 Distribution Plots")
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns

        for col in num_cols:
            st.write(f"**Distribution of {col}**")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
            st.pyplot(fig)

            st.write(f"**Boxplot of {col}**")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.boxplot(x=df[col], ax=ax)
            st.pyplot(fig)

    # 4. Correlation heatmap
    with tab4:
        st.subheader("📌 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # 5. Categorical analysis
    with tab5:
        st.subheader("📌 Categorical Analysis")
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            st.write(f"**Countplot of {col}**")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(x=df[col], ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

            st.write(f"**Value Counts for {col}**")
            st.write(df[col].value_counts())

else:
    st.info("👆 Upload a CSV file to begin EDA")
