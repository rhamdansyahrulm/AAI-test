import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import os
from query import get_data

# Load SQL queries and results using a custom function (get_data) from the 'query' module
query_sql_1, query_result_1 = get_data("query/section_1")

# Configure Streamlit page layout to 'wide'
st.set_page_config(layout="wide")

# Apply custom CSS styling to the Streamlit app using an external style sheet
with open("style.css") as style:
    style_css = style.read()
    st.markdown(f'<style>{style_css}</style>', unsafe_allow_html=True)

# Create a sidebar with a title and subheader for the Streamlit app
st.sidebar.title("Advanced Test Interview")
st.sidebar.subheader("(PT. AA International Indonesia)")

# Define a function to display query results and corresponding SQL code
def display_query_result(query_result, query_sql, header, col):
    col.subheader(header)
    col.dataframe(query_result, hide_index=True)
    with col.expander("See Code"):
        st.code(query_sql)

# Define a dictionary of queries with associated headers for display
queries = {
    'no_1_aai': "No.1",
    'no_2_aai': "No.2",
    'no_3_aai': "No.3",
    'no_4_aai': "No.4",
    'no_5_aai': "Bonus",
}

# Iterate through queries and display results along with SQL code
for query_key, header in queries.items():
    display_query_result(query_result_1[query_key], query_sql_1[query_key], header, st.columns(1)[query_key.endswith('Bonus')])