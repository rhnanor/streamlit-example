import streamlit as st


import streamlit as st

def display_chart(country_name, iframe_code):
    st.title(f"Tourist Arrivals in {country_name}")
    st.write(f"Welcome to the Tourist Arrivals Dashboard for {country_name}. This dashboard provides an interactive visualization of the tourist arrivals data for {country_name}. Explore the chart below to understand the trends and patterns in tourist arrivals over time. The data is sourced from tradingeconomics.com.")
    st.write(iframe_code, unsafe_allow_html=True)
    st.markdown(f"Source: [tradingeconomics.com](https://tradingeconomics.com/{country_name.lower().replace(' ', '-')}/tourist-arrivals)")

# Displaying chart for each country in separate tabs
with st.beta_container():
    st.title("Tourist Arrivals Dashboard")
    st.write("Explore the tourist arrivals data for different countries.")

    with st.beta_tabs("Country Tabs"):
        # Indonesia tab
        with st.beta_container():
            st.write("## Indonesia")
            indonesia_iframe = """
            <iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
            """
            display_chart("Indonesia", indonesia_iframe)

        # Malaysia tab
        with st.beta_container():
            st.write("## Malaysia")
            malaysia_iframe = """
            <iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=malaysiatouarr&v=202304061134V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
            """
            display_chart("Malaysia", malaysia_iframe)

        # Singapore tab
        with st.beta_container():
            st.write("## Singapore")
            singapore_iframe = """
            <iframe src='https://tradingeconomics.com/embed/?s=singaporetouarr&v=202306090122v20230410&h=300&w=600&ref=/singapore/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
            """
            display_chart("Singapore", singapore_iframe)

        # Thailand tab
        with st.beta_container():
            st.write("## Thailand")
            thailand_iframe = """
            <iframe src='https://tradingeconomics.com/embed/?s=thailandtouarr&v=202305260335v20230410&h=300&w=600&ref=/thailand/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
            """
            display_chart("Thailand", thailand_iframe)


