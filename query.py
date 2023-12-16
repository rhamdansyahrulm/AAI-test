import pandas as pd
import os
from google.cloud import bigquery
from google.oauth2 import service_account

def get_data(folder_name):
    """
    Retrieve data from BigQuery based on SQL queries stored in files.

    Parameters:
        - folder_name (str): The name of the folder containing SQL query files.

    Returns:
        - query_sql (dict): A dictionary where keys are query names and values are corresponding SQL queries.
        - query_result (dict): A dictionary where keys are query names and values are DataFrames containing query results.
    """
    # Initialize BigQuery client with service account credentials
    credentials = service_account.Credentials.from_service_account_file("voltaic-reducer-399714-87eda49329ec.json")
    project_id = "voltaic-reducer-399714"
    client = bigquery.Client(credentials=credentials, project=project_id)
    
    # Retrieve data from files in the specified folder
    files = [f for f in os.listdir(os.path.join(os.getcwd(), folder_name)) if os.path.isfile(os.path.join(os.getcwd(), folder_name, f))]
    
    query_sql = {}
    query_result = {}

    # Iterate through each file, read the SQL query, and execute it to get the query result as a DataFrame
    for file in files:
        name = file.split(".")[0]
        file_path = os.path.join(folder_name, file)
        with open(file_path) as f:
            query_sql[name] = f.read()
            query_result[name] = client.query(query_sql[name]).to_dataframe()
            
    return query_sql, query_result