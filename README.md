# 🛡️ Email Spam & Phishing Classifier

An end-to-end Machine Learning and Natural Language Processing (NLP) web application that detects whether an incoming message or email is **Ham (Safe)**, **Spam (Unwanted/Ad)**, or **Phishing (Dangerous/Fraud)**.

## 🚀 Live Demo
🔗 **[Click Here to View the Live Project](PASTE_YOUR_STREAMLIT_APP_URL_HERE)** *(Apni live website ka link yahan paste karein)*

---

## ✨ Features
- **Real-time Detection:** Paste any email text and get instant results.
- **Three-Class Classification:** Unlike basic filters, this handles **Ham**, **Spam**, AND **Phishing** specifically.
- **Clean Web Interface:** Built using Streamlit for an interactive and modern user experience.
- **Production Ready:** Fully deployed and hosted on the cloud.

---

## 🧠 Tech Stack & Concepts Used
- **Language:** Python
- **Framework:** Streamlit (For Web UI)
- **Machine Learning Library:** Scikit-Learn
- **Algorithm:** Multinomial Naive Bayes (Highly efficient for text classification tasks)
- **NLP Technique:** CountVectorizer (Bag of Words model for text tokenization)

---

## 📁 Project Structure
```text
Email-Spam-Classifier/
├── app.py             # Main application file (Model training + Streamlit UI)
├── requirements.txt   # Configuration file containing all necessary libraries
└── README.md          # Project documentation (This file)
```

---

## 🛠️ How to Run Locally

If you want to run this project on your local machine, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate to the project folder:**
   ```bash
   cd Email-Spam-Classifier
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

---

## 📊 How It Works (Behind the Scenes)
1. **Data Ingestion:** The system feeds on a pre-configured text corpus containing verified safe, corporate spam, and phishing samples.
2. **Text Processing:** The `CountVectorizer` removes stop words and converts raw text strings into a mathematical token frequency matrix.
3. **Model Prediction:** The trained `MultinomialNB` classifier evaluates the probabilities of words appearing in specific categories and outputs the highest probability class.

---
💡 **Developed as a 2nd Year Computer Science Project.** Feel free to fork and enhance it!
