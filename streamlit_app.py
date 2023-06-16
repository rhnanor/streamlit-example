import streamlit as st

st.title("Tourist Arrivals in Indonesia")

# Embed the iframe code into the website
iframe_code = "<iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>"
st.markdown(iframe_code, unsafe_allow_html=True)

# Provide the source link
st.markdown("Source: [tradingeconomics.com](https://tradingeconomics.com/indonesia/tourist-arrivals)")
