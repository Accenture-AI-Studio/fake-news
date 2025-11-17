import streamlit as st
import requests
import json

# Load model from HuggingFace
MODEL = "ssva/my_finetuned_deberta"

API_URL = f"https://router.huggingface.co/hf-inference/{MODEL}"



st.title("📰 Fake News Detector")
st.write("Enter the **title** and **article text** and the model will classify whether the news is **TRUE** or **FAKE**.")


#User inputs
user_title = st.text_input("Enter article title here:")
user_text = st.text_area("Enter article text here:")

def query(text):
    response = requests.post(API_URL, json={"inputs": text})
   
    try:
        return response.json()
    except:
        return {"error": "Could not get a valid response from the model."}  
    
    
if st.button("Classify"):
    if user_text.strip() == "" or user_title.strip() == "":
        st.warning("Please enter BOTH a title and some text.")
    else:
        combined_input = user_title+" "+ user_text
        with st.spinner("Classifying..."):
            result = query(combined_input)
           
            if "error" in result:
                if "Loading" in result["error"]:
                    st.info("The model is loading. This may take a while. Please try again in a few moments.")
                else:
                    st.error(result["error"])
            else:
                try:
                    scores = result[0]
                    prob_fake = scores[0]['score']
                    prob_true = scores[1]['score']
                    
                    label = "TRUE" if prob_true > prob_fake else "FAKE"
                    confidence = max(prob_true, prob_fake) 
                    
                    st.subheader(f"Prediction: {label}")
                    st.write(f"Confidence: {confidence:.2%}")
                except Exception as e:
                    st.error("Error processing the model response.")
                    st.write("Raw output", result)              

