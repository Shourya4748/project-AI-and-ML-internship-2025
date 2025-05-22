import streamlit as st
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

st.title("📰 SHOURYA'S Fake News Classifier")

user_input = st.text_area("Enter News Article Text")

if st.button("Classify"):
    cleaned = preprocess(user_input)
    vect_text = vectorizer.transform([cleaned])
    prediction = model.predict(vect_text)[0]
    result = "✅ Real News" if prediction == 1 else "❌ Fake News"
    st.subheader(result)