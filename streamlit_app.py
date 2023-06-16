import streamlit as st
import pandas as pd

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

# Display the selected country and provide a clickable link
st.title(f"Travel Pattern in {selected_country}")
st.write(f"Click [here]({website_links[selected_country]}) to access the travel information for {selected_country}.")
