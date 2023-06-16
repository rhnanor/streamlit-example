import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Main App
def main():
    # Page configuration
    st.set_page_config(page_title="Tourist Arrivals Dashboard", page_icon=":bar_chart:")

    # Displaying chart for each country in separate tabs
    st.title("Tourist Arrivals Dashboard")
    st.write("Explore the tourist arrivals data for different countries.")

    tabs = ["Indonesia", "Malaysia", "Singapore", "Thailand", "User Feedback"]
    selected_tab = st.selectbox("Select a tab", tabs)

tabs = ["Indonesia", "Malaysia", "Singapore", "Thailand"]
selected_tab = st.selectbox("Select a country", tabs)

if selected_tab == "Indonesia":
    st.write("## Indonesia")
    indonesia_iframe = """
    <iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=indonesiatouarr&v=202306050459V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
    """
    display_chart("Indonesia", indonesia_iframe)
elif selected_tab == "Malaysia":
    st.write("## Malaysia")
    malaysia_iframe = """
    <iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=malaysiatouarr&v=202304061134V20230410&h=300&w=600' height='300' width='600' frameborder='0' scrolling='no'></iframe>
    """
    display_chart("Malaysia", malaysia_iframe)
elif selected_tab == "Singapore":
    st.write("## Singapore")
    singapore_iframe = """
    <iframe src='https://tradingeconomics.com/embed/?s=singaporetouarr&v=202306090122v20230410&h=300&w=600&ref=/singapore/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
    """
    display_chart("Singapore", singapore_iframe)
elif selected_tab == "Thailand":
    st.write("## Thailand")
    thailand_iframe = """
    <iframe src='https://tradingeconomics.com/embed/?s=thailandtouarr&v=202305260335v20230410&h=300&w=600&ref=/thailand/tourist-arrivals' height='300' width='600' frameborder='0' scrolling='no'></iframe>
    """
    display_chart("Thailand", thailand_iframe)
elif selected_tab == "User Feedback":
    st.write("## User Feedback")
    st.write("Have something to say about the Tourist Arrivals Dashboard? Share your feedback with us!")
    st.write("Enter your feedback in the sidebar on the left and click 'Submit'.")

# Function to display chart
def display_chart(country_name, iframe):
    st.markdown(iframe, unsafe_allow_html=True)
    st.write(f"Source: [tradingeconomics.com]({get_data_source_link(country_name)})")


    # User Feedback and Sentiment Analysis
    if selected_tab == "User Feedback":
        st.write("## User Feedback")
        st.write("Have something to say about the Tourist Arrivals Dashboard? Share your feedback with us!")
        st.write("Enter your feedback in the sidebar on the left and click 'Submit'.")

        user_feedback = st.text_area("Enter your feedback here:")
        if st.button("Submit"):
            sentiment_score = analyze_sentiment(user_feedback)
            if sentiment_score > 0:
                st.success("Thank you for your positive feedback!")
            elif sentiment_score < 0:
                st.error("We're sorry to hear that you're not satisfied. Please provide more details.")
            else:
                st.info("We appreciate your feedback. We'll take it into consideration for improvement.")

    # Function to analyze sentiment
    def analyze_sentiment(text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        return sentiment


if __name__ == "__main__":
    main()
