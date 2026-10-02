import pickle
from pathlib import Path

import streamlit as st

# Load the vectorizer and model from the trained model folder
base_dir = Path(__file__).resolve().parent.parent
model_dir = base_dir / "Our_Trained_Model"

with open(model_dir / "vectorizer.sav", "rb") as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

with open(model_dir / "trained_model.sav", "rb") as model_file:
    loaded_model = pickle.load(model_file)

st.title("Twitter Sentiment Analysis")
st.write("Enter a tweet to classify it as Positive or Negative.")

user_input = st.text_area("Tweet", "This is an amazing day!")

if st.button("Predict Sentiment"):
    cleaned_tweet = loaded_vectorizer.transform([user_input])
    prediction = loaded_model.predict(cleaned_tweet)
    sentiment = "Positive" if prediction[0] == 1 else "Negative"

    if sentiment == "Positive":
        st.success(f"Prediction: {sentiment}")
    else:
        st.error(f"Prediction: {sentiment}")