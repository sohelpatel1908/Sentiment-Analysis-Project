import pickle
import streamlit as st
import re


def clean_tweet(tweet):
  # Converting text/string to lowercase so it can treat words same like "Goat" and "goat"
  tweet = tweet.lower()
  # Removing Hashtags
  tweet = re.sub(r'#\S+', '', tweet)
  # Removing Mentions
  tweet = re.sub(r'@\S+', '', tweet)
  # Removing URLs
  tweet = re.sub(r'(\S+)?https?:\S+|www?\S+|\S+.com\S+', '', tweet)
  # Removing Special Characters
  # tweet = re.sub(r'[!\-@#$%^*_()/.,:&]', '', tweet)
  tweet = re.sub(r'[^(\w\d\s)]', '', tweet)
  # Stripping Rows
  tweet = tweet.strip()
  # Handling Inconsistant Whitespaces
  tweet = re.sub(r'\s{2,}', ' ', tweet)
  # Retrieving cleaned tweet
  return tweet

def predict(tweet):
    cleaned_tweet = clean_tweet(tweet)
    vectorized_tweet = vectorizer.transform([cleaned_tweet])
    prediction = sentiment_model.predict(vectorized_tweet)

    if prediction == 0: 
        st.write("### :rainbow[Negative Sentiment]🥲")
    elif prediction == 4:
        st.write("### :rainbow[Positive Sentiment]😃")
    else:
        st.write("### 😐:rainbow[*Neutral*]😑")
        st.snow()

# Importing pickle files
with open('Deployed Model/Logistic_regression_sentiment.pkl', 'rb') as file:
    sentiment_model = pickle.load(file)
with open('Deployed Model/vectorized_vocab.pkl', 'rb') as vector:
    vectorizer = pickle.load(vector)

st.title(":rainbow[**Sentiment Analysis of Tweets**]")

# Receiving text from user
tweet = st.text_input("Enter your tweets")
print("User entered: ", tweet)

# Predicting Sentiment: Positive or Negative
if st.button("Predict"):
    predict(tweet)
