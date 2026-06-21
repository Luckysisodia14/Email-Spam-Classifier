"""
Email/SMS Spam & Phishing Classifier - Web Application
Author: 2nd Year B.Tech Student Project
Description: Clean Streamlit Frontend for our trained NLP Model.
"""

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Page Configuration (Website ka title aur icon)
st.set_page_config(page_title="Email Safeguard AI", page_icon="🛡️", layout="centered")


@st.cache_resource
def train_and_get_model():
    """Dataset ko load aur model ko train karke vectorizer aur model return karta hai."""
    data = {
        'message': [
            # Safe / Ham
            "Hey, are we still meeting for lunch tomorrow at 1 PM?",
            "Please find attached the quarterly project report for your review.",
            "Can you send me the notes from today's computer science lecture?",
            "Thanks for the update, I will submit the assignment by Monday.",
            "Are you free this weekend for a quick project discussion?",
            # Spam
            "Congratulations! You've won a free $1000 Walmart gift card. Click here now!",
            "Get cheap luxury watches at 90% off! Limited time discount offer!",
            "Double your cash instantly! Guaranteed financial returns within 24 hours.",
            "Dear Friend, claim your inheritance money right now by replying to this ad.",
            "Buy online medicine today without a doctor note. Fast delivery worldwide.",
            # Phishing
            "URGENT: Your bank account has been compromised. Log in immediately to verify identity.",
            "Official Notice from IT: Your password expires in 24 hours. Update your credentials here.",
            "Security Alert: Unauthorized login attempt detected on your Netflix account. Click to reset.",
            "Dear customer, your credit card is blocked. Reactivate it now by entering your OTP.",
            "Your tax refund of $500 is ready. Click the official government link to claim now."
        ],
        'label': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    }
    df = pd.DataFrame(data)
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['message'])
    y = df['label']
    
    model = MultinomialNB()
    model.fit(X, y)
    return vectorizer, model

# Model train karke load karo
vectorizer, model = train_and_get_model()

# 2. Frontend UI Layout Design
st.title("🛡️ Email Spam & Phishing Classifier")
st.subheader("Developed for 2nd Year Project Submission")
st.write("Apna email ya message niche box mein paste kijiye aur check kijiye ki woh safe hai ya nahi.")

# User input text box
user_input = st.text_area("✍️ Enter Email/SMS Content Here:", placeholder="Type or paste your message text here...")

# Predict button
if st.button("🔍 Scan Message", type="primary"):
    if user_input.strip() == "":
        st.warning("⚠️ Kripya pehle kuch text enter karein!")
    else:
        # Text ko numbers mein convert karke predict karna
        vectorized_text = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_text)
        
        # UI par result display karna colors ke sath
        st.write("---")
        st.subheader("📊 Analysis Result:")
        
        if prediction == 0:
            st.success("🟢 **HAM (SAFE EMAIL)**: Yeh email bilkul safe lag raha hai. Aap ispar trust kar sakte hain.")
        elif prediction == 1:
            st.warning("🟡 **SPAM ALERT**: Yeh ek unsolicited advertisement ya promotion lag raha hai.")
        else:
            st.error("🔴 **PHISHING ATTACK DETECTED**: Yeh ek bohot hi dangerous scam/fraud email lag raha hai. Kisi link par click mat karna!")
