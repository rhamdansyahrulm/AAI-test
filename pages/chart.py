import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import matplotlib.pyplot as plt
import altair as alt
import os
from query import get_data
from chart_function import *

# Load SQL queries and results using a custom function (get_data) from the 'query' module
query_sql_2, query_result_2 = get_data("query/section_2")

# Configure Streamlit page layout to 'wide'
st.set_page_config(layout="wide")

# Apply custom CSS styling to the Streamlit app using an external style sheet
with open("style.css") as style:
    style_css = style.read()
    st.markdown(f'<style>{style_css}</style>', unsafe_allow_html=True)

# Create a sidebar with a title and subheader for the Streamlit app
st.sidebar.title("Advanced Test Interview")
st.sidebar.subheader("(PT. AA International Indonesia)")

# Display overall dashboard information in the first container
with st.container():
    # Calculate and display total information about hospitals and members
    total_hospital = query_result_2["hospital"].shape[0]
    total_member = query_result_2["member"].shape[0]
    total_admission = query_result_2["hospital"]["frequency"].sum()
    total_balance = query_result_2["member"]["balance"].sum()
    total_amount = query_result_2["member"]["total_amount"].sum()
    
    # Display the title and information board
    title_spot, board_location = st.columns(2)
    title_spot.title("AAI TEST DASHBOARD")
    
    # Display board information using a loop
    board_information_title = ["TOTAL HOSPITAL", "TOTAL MEMBER", "TOTAL ADMISION", "TOTAL BALANCE", "TOTAL AMOUNT"]
    board_information_values = [total_hospital, total_member, total_admission, "$"+str(total_balance), "$"+str(total_amount)]
    i = 0
    
    for col in board_location.columns(5):
        add_board_information(col, board_information_title[i], board_information_values[i])
        i += 1

# Display charts related to hospital data in the second container
with st.container():
    # Create charts for hospital-related data
    hospital_amount = create_bar_chart(query_result_2["hospital"], 'hospital_name', 'total_amount')
    admission_series = line_dual_axis(query_result_2["time_series"], 'admission_date', 'total_amount', 'frequency')
    hospital_admission = create_bar_chart(query_result_2["hospital"], 'hospital_name', 'frequency')
    
    # Display the title and charts for hospital-related data using a loop
    i = 0
    hospital_data_title = ["HOSPITAL AMOUNT", "MEMBER ADMISSION", "HOSPITAL ADMISSION"]
    hospital_data_values = [hospital_amount, admission_series, hospital_admission]
    
    for col in st.columns(3):
        chart_spot(col, hospital_data_title[i])
        
        # Shift the chart further to the right
        left, right = col.columns((1, 20))
        right.altair_chart(hospital_data_values[i], use_container_width=False)        
        i += 1

# Display charts related to member data in the third container
with st.container():
    # Create charts for member-related data
    balance_category = create_bar_chart(data=query_result_2["member"], x='balance', categorize=True)
    amount_category = create_bar_chart(data=query_result_2["member"], x='total_amount', categorize=True)
    status_category = donut_chart(query_result_2["member"], "status")
    
    # Display the title and charts for member-related data using a loop
    i = 0
    hospital_data_title = ["BALANCE DISTRIBUTION", "MEMBER STATUS", "AMOUNT DISTRIBUTION"]
    hospital_data_values = [balance_category, status_category, amount_category]
    
    for col in st.columns(3):
        chart_spot(col, hospital_data_title[i])
        
        # Shift the chart further to the right
        left, right = col.columns((1, 20))
        if hospital_data_values[i] is not None:
            right.altair_chart(hospital_data_values[i], use_container_width=False)        
        i += 1
