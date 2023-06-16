import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("travel_data.csv")  # Replace "travel_data.csv" with your actual data file

# Create a sidebar for user input
st.sidebar.title("Travel Pattern Explorer")
selected_country = st.sidebar.selectbox("Select a Country", data["Country"].unique())

# Filter the data based on the selected country
country_data = data[data["Country"] == selected_country]

# Display basic information about the country
st.title(f"Travel Pattern in {selected_country}")
total_visits = country_data["Visits"].sum()
st.write(f"Total Visits: {total_visits}")

# Visualize the travel pattern using a line plot
plt.figure(figsize=(10, 6))
plt.plot(country_data["Year"], country_data["Visits"])
plt.xlabel("Year")
plt.ylabel("Visits")
plt.title("Travel Pattern Over Time")
st.pyplot()

# Display a table with detailed data
st.subheader("Detailed Data")
st.dataframe(country_data)

# Add more interactive elements and analysis as needed
# For example, you can allow users to select specific years or regions within a country,
# provide statistical summaries, or incorporate interactive maps for visualization.

