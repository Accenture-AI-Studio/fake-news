import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model from HuggingFace
model_name = "ssva/my_finetuned_deberta"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

st.title("📰 Fake News Detector")
st.write("Enter a news article and I will classify it as **TRUE** or **FAKE**.")

user_text = st.text_area("Enter article text here:")

if st.button("Classify"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Tokenize
        encoding = tokenizer(
            user_text,
            truncation=True,
            padding=True,
            max_length=512,
            return_tensors="pt"
        )

        # Model prediction
        with torch.no_grad():
            output = model(**encoding)

        logits = output.logits
        probabilities = torch.softmax(logits, dim=1)
        prob_fake = probabilities[0][0].item()
        prob_true = probabilities[0][1].item()

        label = "TRUE" if prob_true > prob_fake else "FAKE"
        confidence = max(prob_true, prob_fake)

        st.subheader(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence:.2%}**")
