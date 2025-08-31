import pandas as pd
import streamlit as st
import time
st.sidebar.title("Sidebar   ")
st.title("CSV File Uploader")

# File uploader widget
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    st.sidebar.success("file loaded succesfully!")
    df=pd.read_csv(uploaded_file)
    n=st.text_input("Number of Records")
    click=st.button("View CSV")
    if click:
        with st.spinner(text="Loading..", show_time=False, width="content"):
            time.sleep(2.5)
        if n.isnumeric():
            st.dataframe(df.head(int(n)))
