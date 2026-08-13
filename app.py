import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data once
@st.cache_resource
def load_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    return True

# Initialize resources with caching for better performance
@st.cache_resource
def initialize_resources():
    load_nltk_resources()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    custom_remove = {'subject'}
    return ps, stop_words, punctuation, custom_remove

@st.cache_resource
def load_models():
    try:
        tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
        model = pickle.load(open('stacking_model.pkl', 'rb'))
        return tfidf, model
    except FileNotFoundError as e:
        st.error(f"Error loading model files: {e}")
        return None, None

# Initialize
ps, stop_words, punctuation, custom_remove = initialize_resources()
tfidf, model = load_models()

if tfidf is None or model is None:
    st.stop()  # Stop if models didn't load

def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    
    transformed_tokens = [
        ps.stem(token)
        for token in tokens
        if token.isalnum()
        and token not in stop_words
        and token not in punctuation
        and token not in custom_remove
    ]
    
    return " ".join(transformed_tokens)

# UI
st.title("Email Spam Classifier")
input_sms = st.text_area("Enter the message", height=150)

if st.button('Predict', type="primary"):
    # Validate input
    if not input_sms.strip():
        st.warning("Please enter a message to classify")
    else:
        try:
            # 1. Preprocess
            transformed_sms = transform_text(input_sms)
            
            # 2. Vectorize
            vector_input = tfidf.transform([transformed_sms])
            
            # 3. Predict
            result = model.predict(vector_input.toarray())[0]
            
            # 4. Display result
            if result == 1:
                st.error("🚨 **SPAM**")
            else:
                st.success("✅ **NOT SPAM**")
                
        except Exception as e:
            st.error(f"Error during prediction: {e}")