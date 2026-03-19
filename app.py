import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# 1. Setup Page Config
st.set_page_config(page_title="Movie Sentiment AI", page_icon="🎬", layout="centered")

# 2. Load the Model and Vectorizer
@st.cache_resource
def load_assets():
    model = pickle.load(open('model.pkl', 'rb'))
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    return model, tfidf

model, tfidf = load_assets()
ps = PorterStemmer()

# 3. Preprocessing Function (Must match your Colab logic)
def clean_text(text):
    text = re.sub(r'<.*?>', '', text) # Remove HTML
    text = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    stop_words = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves']) # Simplified for GUI speed
    text = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

# 4. GUI Layout
st.title("🎬 Movie Review Sentiment Analyzer")
st.markdown("---")
st.write("Enter a movie review below to analyze its sentiment using our **Linear Model (90.5% Accuracy)**.")

user_input = st.text_area("Write your review here...", height=150, placeholder="The cinematography was brilliant, but the plot was weak.")

if st.button("Predict Sentiment"):
    if user_input.strip():
        # Process input
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        
        # Display Result
        st.markdown("### Result:")
        if prediction == 1:
            st.success("✨ **POSITIVE SENTIMENT**")
            st.balloons()
        else:
            st.error("📉 **NEGATIVE SENTIMENT**")
    else:
        st.warning("Please enter some text first!")

st.markdown("---")
st.caption("Developed as part of Practical 8 - NLP Sentiment Analysis Project.")