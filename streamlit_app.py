import streamlit as st
from streamlit import components

st.title("Tourist Arrivals in Indonesia")

# Embed the bar chart into the website using an iframe
iframe_code = "<iframe src='https://tradingeconomics.com/embed/?s=indonesiatouarr&v=202306050459v20230410&h=300&w=600&ref=/indonesia/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>"
components.html(iframe_code)

# Provide the source link
st.markdown("Source: [tradingeconomics.com](https://tradingeconomics.com/indonesia/tourist-arrivals)")
