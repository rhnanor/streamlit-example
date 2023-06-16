import streamlit as st
import pandas as pd
import altair as alt

# Dictionary of country names and their corresponding data links
country_links = {
    'Indonesia': 'https://tradingeconomics.com/indonesia/tourist-arrivals',
    'Malaysia': 'https://tradingeconomics.com/malaysia/tourist-arrivals',
    'Thailand': 'https://tradingeconomics.com/thailand/tourist-arrivals'
    # Add more countries and their links here
}

# Function to load data from the given link
def load_data(link):
    data = pd.read_html(link)[0]
    # Perform any necessary data preprocessing
    return data

# Function to create a bar chart using Altair
def create_bar_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        x='Year',
        y='Tourist Arrivals',
        tooltip=['Year', 'Tourist Arrivals']
    ).properties(
        width=600,
        height=400
    )
    return chart

# Main app code
st.title("Tourist Arrivals by Country")

# Select the country
selected_country = st.selectbox("Select a country", list(country_links.keys()))

# Load data for the selected country
data = load_data(country_links[selected_country])

# Create and display the bar chart
chart = create_bar_chart(data)
st.altair_chart(chart, use_container_width=True)
st.altair_chart(chart, use_container_width=True)
