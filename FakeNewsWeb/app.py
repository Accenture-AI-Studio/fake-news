import streamlit as st
import pickle
import os
import numpy as np


# Load model from Files
MODEL = "Models"



def load_model():
    with open(os.path.join(MODEL, "logistic_regression.pkl"), "rb") as f:
        model = pickle.load(f)
    with open(os.path.join(MODEL, "tfidf_vectorizer.pkl"), "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

model, vectorizer = load_model()
    
st.title("📰 Fake News Detector")
st.write("Enter the **title** and **article text** and the model will classify whether the news is **TRUE** or **FAKE**.")


#User inputs
user_title = st.text_input("Enter article title here:")
user_text = st.text_area("Enter article text here:")


    
if st.button("Classify"):
    if not user_text.strip() or not user_title.strip():
        st.warning("Please enter BOTH a title and some text.")
    else:
        combined_input = " [TITLE] " + user_title + " [ARTICLE] " + user_text
        
        X = vectorizer.transform([combined_input])
        
        probs = model.predict_proba(X)[0]
        prob_fake = probs[0]
        prob_true = probs[1]
        label = "TRUE" if prob_true > prob_fake else "FAKE"
        confidence = max(prob_true, prob_fake) 
                    
        st.subheader(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence:.2%}**")
                     

