# 🐦 Twitter Sentiment Analysis Project

## 📌 Project Overview
This project is an end-to-end Machine Learning solution that analyzes the sentiment of tweets (Positive vs. Negative). It uses the **Sentiment140** dataset (1.6 million tweets) to train a **Logistic Regression** model and is deployed as a web application using **Streamlit**.

## 🚀 Live Demo
*https://sentiment-analysis-project-3pbz64weuvg5jbnmyyjxgy.streamlit.app/*

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy)
- **Machine Learning** (Scikit-Learn, Logistic Regression)
- **NLP** (NLTK, TF-IDF Vectorization)
- **Visualization** (Matplotlib, Seaborn)
- **Deployment** (Streamlit)

## 📊 Key Features
- **Data Preprocessing:** Cleaning text using Regex (removing URLs, @mentions, hashtags).
- **Visualization:** Trend analysis of sentiment over time and specific keyword insights.
- **Model:** Logistic Regression achieving high accuracy on test data.
- **App:** Real-time sentiment prediction interface.

## 📂 Dataset
The dataset used is the [Sentiment140 Dataset from Kaggle](https://www.kaggle.com/kazanova/sentiment140).
*(Note: The dataset is not included in this repo due to size constraints.)*

## 🚀 What Can Be Improved? (Future Improvements🔧):
➕ **Advanced Embedding:** Moving from TF-IDF to Sentence Transformers (all-MiniLM-L6-v2) for better semantic understanding.
➕ **Deep Learning:** Implementing LSTMs or BERT to better capture long-term dependencies in complex tweets.
➕ **Comparing Algorithms:** Comparing Logistic Regression against Random Forest and Naive Bayes for better speed and accuracy.
