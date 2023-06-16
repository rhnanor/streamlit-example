import streamlit as st

st.title("Tourist Arrivals in Indonesia")
st.write("Welcome to the Tourist Arrivals Dashboard for Indonesia. This dashboard provides an interactive visualization of the tourist arrivals data for Indonesia. Explore the chart below to understand the trends and patterns in tourist arrivals over time. The data is sourced from tradingeconomics.com.")


# HTML code to embed the iframe
iframe_code = """
<iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
"""

# Display the iframe using the HTML code
st.write(iframe_code, unsafe_allow_html=True)

# Provide the source link
st.markdown("Source: [tradingeconomics.com](https://tradingeconomics.com/indonesia/tourist-arrivals)")
