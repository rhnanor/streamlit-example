import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from the website
data_link = "https://tradingeconomics.com/indonesia/tourist-arrivals"
data = pd.read_html(data_link)[0]

# Clean and preprocess the data if needed
# (extract the necessary columns, handle missing values, etc.)

# Create a bar chart using Plotly
fig = px.bar(data, x='Year', y='Tourist Arrivals', labels={'Tourist Arrivals': 'Tourist Arrivals'}, title='Tourist Arrivals in Indonesia')

# Display the bar chart in Streamlit
st.plotly_chart(fig)
