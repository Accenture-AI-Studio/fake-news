import streamlit as st
import pickle
import os
import numpy as np
from cleaning import full_clean_text


# Load model from Files
BASE_DIR = os.path.dirname(__file__)
MODELS_DIR = os.path.join(BASE_DIR, "Models")



def load_model():
    model_path = os.path.join(MODELS_DIR, "logistic_regression.pkl")
    
    vectorizer_path = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(vectorizer_path, "rb") as f:
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
        clean_title = full_clean_text(user_title)
        clean_text = full_clean_text(user_text)
        combined_input = " [TITLE] " + clean_title + " [ARTICLE] " + clean_text
        
        X = vectorizer.transform([combined_input])
        
        probs = model.predict_proba(X)[0]
        prob_fake = probs[0]
        prob_true = probs[1]
        label = "TRUE" if prob_true > prob_fake else "FAKE"
        confidence = max(prob_true, prob_fake) 
                    
        st.subheader(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence:.2%}**")
                     

