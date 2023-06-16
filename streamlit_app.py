import streamlit as st
import pandas as pd

# Function to load travel data from a website link
def load_data(link):
    data = pd.read_csv(link)  # Replace with appropriate code to load data from the website link
    return data

# Define website links for travel data
website_links = {
    "Thailand": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
    "Malaysia": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
    "Indonesia": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
    "Vietnam": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main"
}

# Create a sidebar for user input
st.sidebar.title("Travel Pattern Explorer")
selected_country = st.sidebar.selectbox("Select a Country", list(website_links.keys()))

# Load data based on the selected country
data_link = website_links[selected_country]
data = load_data(data_link)

# Display basic information about the country
st.title(f"Travel Pattern in {selected_country}")
total_visits = data["Visits"].sum()
st.write(f"Total Visits: {total_visits}")

# Display the data table
st.subheader("Data Table")
st.dataframe(data)
