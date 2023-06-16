import streamlit as st
import pandas as pd
import altair as alt

# Load data from the website
data_link = "https://tradingeconomics.com/indonesia/tourist-arrivals"
data = pd.read_html(data_link)[0]

# Clean and preprocess the data if needed
# (extract the necessary columns, handle missing values, etc.)

# Create a bar chart using Altair
chart = alt.Chart(data).mark_bar().encode(
    x='Year',
    y='Tourist Arrivals',
    tooltip=['Year', 'Tourist Arrivals']
).properties(
    title='Tourist Arrivals in Indonesia'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
