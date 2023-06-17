import streamlit as st
from textblob import TextBlob

# Main App
def main():
    # Page configuration
    st.set_page_config(page_title="Tourist Arrivals Dashboard", page_icon=":bar_chart:")

    # Displaying chart for each country in separate tabs
    st.title("Tourist Arrivals Dashboard")
    st.write("Explore the tourist arrivals data for different countries.")

    tabs = ["Indonesia", "Malaysia", "Singapore", "Thailand", "User Feedback"]
    selected_tab = st.selectbox("Select a tab", tabs)

    if selected_tab == "Indonesia":
        display_chart("Indonesia", "indonesia_iframe")
    elif selected_tab == "Malaysia":
        display_chart("Malaysia", "malaysia_iframe")
    elif selected_tab == "Singapore":
        display_chart("Singapore", "singapore_iframe")
    elif selected_tab == "Thailand":
        display_chart("Thailand", "thailand_iframe")
    elif selected_tab == "User Feedback":
        display_user_feedback()


# Function to display chart
def display_chart(country_name, iframe_variable_name):
    st.write(f"## {country_name}")
    iframe_code = st.secrets[iframe_variable_name]
    st.markdown(iframe_code, unsafe_allow_html=True)
    st.markdown(f"Source: [tradingeconomics.com](https://tradingeconomics.com/{country_name.lower().replace(' ', '-')}/tourist-arrivals)")


# Function to display user feedback
def display_user_feedback():
    st.write("## User Feedback")
    st.write("Have something to say about the Tourist Arrivals Dashboard? Share your feedback with us!")
    st.write("Enter your feedback in the text box below and click 'Submit'.")

    feedback = st.text_input("Enter your feedback on the helpfulness of this website:")
    if st.button("Submit"):
        if feedback:
            blob = TextBlob(feedback)
            sentiment_score = blob.sentiment.polarity
            sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

            st.markdown(f"*Feedback:* {feedback}")
            st.markdown(f"*Sentiment Score:* {sentiment_score:.2f}")
            st.markdown(f"*Sentiment:* {sentiment_label}")
        else:
            st.warning("Please enter your feedback before submitting.")
