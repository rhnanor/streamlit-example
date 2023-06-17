import streamlit as st
from textblob import TextBlob
from PIL import Image
import requests
from io import BytesIO

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
        display_chart("Indonesia")
    elif selected_tab == "Malaysia":
        display_chart("Malaysia")
    elif selected_tab == "Singapore":
        display_chart("Singapore")
    elif selected_tab == "Thailand":
        display_chart("Thailand")
    elif selected_tab == "User Feedback":
        display_user_feedback()


# Function to display chart
def display_chart(country_name):
    st.write(f"## {country_name}")
    placeholder_image = f"{country_name.lower()}_chart.png"
    st.image(placeholder_image, use_column_width=True)
    st.markdown(f"Source: [tradingeconomics.com](https://tradingeconomics.com/{country_name.lower().replace(' ', '-')}/tourist-arrivals)")

# Function to get the chart image URL for each country
def get_chart_image_url(country_name):
    if country_name == "Indonesia":
        return "https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600"
    elif country_name == "Malaysia":
        return "https://d3fy651gv2fhd3.cloudfront.net/embed/?s=malaysiatouarr&v=202304061134V20230410&h=300&w=600"
    elif country_name == "Singapore":
        return "https://tradingeconomics.com/embed/?s=singaporetouarr&v=202306090122v20230410&h=300&w=600&ref=/singapore/tourist-arrivals"
    elif country_name == "Thailand":
        return "https://tradingeconomics.com/embed/?s=thailandtouarr&v=202305260335v20230410&h=300&w=600&ref=/thailand/tourist-arrivals"

# Function to load image from URL
def load_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    return image

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


if __name__ == "__main__":
    main()
