import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import matplotlib.pyplot as plt
import altair as alt

# Define functions for creating and displaying information boards and charts

def add_board_information(col, title, value):
    """
    Adds an information board to the Streamlit app displaying a title and corresponding value.

    Parameters:
        - col (streamlit.columns): The Streamlit column where the board information will be added.
        - title (str): The title of the information board.
        - value (str): The value to be displayed on the information board.
    """
    board_information_script = f'''
    <div class="board_information">
        <p class="board_information_title">{title}</p>
        <p class="board_information_value">{value}</p>
    </div>
    '''
    col.markdown(board_information_script, unsafe_allow_html=True)

def chart_spot(col, title):
    """
    Adds a chart title to the Streamlit app.

    Parameters:
        - col (streamlit.columns): The Streamlit column where the chart title will be added.
        - title (str): The title of the chart.
    """
    board_information_script = f'''
    <div class="hospital_data">
        <p class="hospital_data_title">{title}</p>
    </div>
    '''
    col.markdown(board_information_script, unsafe_allow_html=True)

def create_bar_chart(data, x, y=None, categorize=False):
    """
    Creates a bar chart using Altair.

    Parameters:
        - data (pd.DataFrame): The DataFrame containing the data for the chart.
        - x (str): The column name for the x-axis.
        - y (str): The column name for the y-axis.
        - categorize (bool): If True, categorizes the data based on specified conditions.

    Returns:
        - viz_bar (alt.Chart): The Altair bar chart.
    """
    if categorize:
        data['category'] = data[x].apply(lambda x: '0-150' if x <= 150 else ('150-300' if x < 300 else '>=300'))
        category_counts = data.groupby('category').size().reset_index(name='count')
        x, y = 'category', 'count'
    
    viz_bar = alt.Chart(category_counts if categorize else data).mark_bar().encode(
            x=alt.X(str(x), title=None, axis=alt.Axis(labelAngle=0)), 
            y=alt.Y(y, title='Total')
    ).properties(width=400, height=180)
    
    return viz_bar

def line_dual_axis(data, x, y1, y2):
    """
    Creates a dual-axis line chart using Altair.

    Parameters:
        - data (pd.DataFrame): The DataFrame containing the data for the chart.
        - x (str): The column name for the x-axis.
        - y1 (str): The column name for the primary y-axis.
        - y2 (str): The column name for the secondary y-axis.

    Returns:
        - line_chart (alt.Chart): The Altair dual-axis line chart.
    """
    data['admission_date'] = data['admission_date'].map(lambda tanggal: pd.to_datetime(tanggal).strftime('%m/%d'))
    base = alt.Chart(data).encode(
        alt.X(x, title=None, axis=alt.Axis(labelAngle=0))
    )

    line1 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y(y1).title('Amount', titleColor='#5276A7')
    )

    line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y(y2).title('frequency', titleColor='#5276A7')
    )

    line_chart = alt.layer(line1, line2).resolve_scale(
        y='independent'
    ).properties(width=410, height=180)
    
    return line_chart

def donut_chart(data, x):
    """
    Creates a donut chart using Altair.

    Parameters:
        - data (pd.DataFrame): The DataFrame containing the data for the chart.
        - x (str): The column name for encoding the chart.

    Returns:
        - combined_chart (alt.Chart): The Altair donut chart with labels.
    """
    category_counts = data.groupby(x).size().reset_index(name='count')

    chart = alt.Chart(category_counts).mark_arc(innerRadius=50).encode(
        theta='count',
        color=alt.Color(f"{x}:N"),
    ).properties(
        width=400,
        height=180
    )

    caption_text = ["Y : Amount > Balance", "N : Amount < Balance"]

    caption = alt.Chart(category_counts).mark_text(
        align='center',
        baseline='middle',
        fontSize=10,
    ).encode(
        text=alt.value(caption_text)
    )

    combined_chart = chart + caption

    return combined_chart
