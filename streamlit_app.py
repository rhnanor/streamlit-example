import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the website
data_link = "https://tradingeconomics.com/indonesia/tourist-arrivals"
data = pd.read_html(data_link)[0]

# Clean and preprocess the data if needed
# (extract the necessary columns, handle missing values, etc.)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Year'], data['Tourist Arrivals'])
plt.xlabel('Year')
plt.ylabel('Tourist Arrivals')
plt.title('Tourist Arrivals in Indonesia')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the bar chart in Streamlit
st.pyplot(plt)
