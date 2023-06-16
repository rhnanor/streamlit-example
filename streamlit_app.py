import streamlit as st
import pandas as pd

# Define website links and corresponding images for travel data
website_links = {
    "Thailand": {
        "link": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
        "image": "thailand.png"
    },
    "Malaysia": {
        "link": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
        "image": "malaysia.png"
    },
    "Indonesia": {
        "link": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
        "image": "indonesia.png"
    },
    "Vietnam": {
        "link": "https://public.tableau.com/app/profile/tan.zhi.xuan/viz/TouristArrivalsForecatingDashboardBasedonCovid-19/Main",
        "image": "vietnam.png"
    }
}

# Create a sidebar for user input
st.sidebar.title("Travel Pattern Explorer")
selected_country = st.sidebar.selectbox("Select a Country", list(website_links.keys()))

# Display the selected country with the associated image and clickable link
st.title(f"Travel Pattern in {selected_country}")
image_path = website_links[selected_country]["image"]
image = open(image_path, "rb")
st.image(image, caption=f"{selected_country} Data Visualization")
st.write(f"Click [here]({website_links[selected_country]['link']}) to access the travel information for {selected_country}.")
