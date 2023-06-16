import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Function to analyze sentiment of user feedback
def analyze_sentiment(feedback):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(feedback)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function to display the sentiment analysis results
def display_sentiment_analysis(feedback):
    sentiment = analyze_sentiment(feedback)
    
    st.subheader("User Feedback Sentiment Analysis")
    st.write(f"Feedback: {feedback}")
    st.write(f"Sentiment: {sentiment}")

# Function to display the chart and description
def display_chart(country_name, iframe_code):
    st.title(f"Tourist Arrivals in {country_name}")
    st.write(f"Welcome to the Tourist Arrivals Dashboard for {country_name}. This dashboard provides an interactive visualization of the tourist arrivals data for {country_name}. Explore the chart below to understand the trends and patterns in tourist arrivals over time. The data is sourced from tradingeconomics.com.")
    st.write(iframe_code, unsafe_allow_html=True)
    st.markdown(f"Source: [tradingeconomics.com](https://tradingeconomics.com/{country_name.lower().replace(' ', '-')}/tourist-arrivals)")

# Displaying chart for Indonesia
indonesia_iframe = """
<iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
"""
display_chart("Indonesia", indonesia_iframe)

# Displaying chart for Malaysia
malaysia_iframe = """
<iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=malaysiatouarr&v=202304061134V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
"""
display_chart("Malaysia", malaysia_iframe)

# Displaying chart for Singapore
singapore_iframe = """
<iframe src='https://tradingeconomics.com/embed/?s=singaporetouarr&v=202306090122v20230410&h=300&w=600&ref=/singapore/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
"""
display_chart("Singapore", singapore_iframe)

# Displaying chart for Thailand
thailand_iframe = """
<iframe src='https://tradingeconomics.com/embed/?s=thailandtouarr&v=202305260335v20230410&h=300&w=600&ref=/thailand/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
"""
display_chart("Thailand", thailand_iframe)


