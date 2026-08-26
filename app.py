import streamlit as st

st.write("Python environment test")

try:
    import gdown
    st.success(f"gdown imported successfully: {gdown.__version__}")
except Exception as e:
    st.error(f"gdown import failed: {e}")

st.stop()
# import streamlit as st
# import pickle
# import string
# import os
# import gdown
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# # 1. Download required NLTK data securely once
# @st.cache_resource
# def load_nltk_resources():
#     # Fix for modern NLTK installations requiring punkt_tab
#     for resource in ['punkt', 'punkt_tab', 'stopwords']:
#         try:
#             nltk.download(resource, quiet=True)
#         except Exception:
#             pass
#     return True

# # 2. Auto-download and cache large model files from Google Drive
# @st.cache_resource
# def download_and_load_models():
#     # Google Drive file IDs
#     vectorizer_id = '1QHiityuQD78RrMoTf5RESsGDa-QfpPNv' 
#     model_id = '19bGiKPG0M3Pcy-ca0pV-kqGAeebmDBtM'  

#     vec_output = 'vectorizer.pkl'
#     model_output = 'stacking_model.pkl'

#     # Download Vectorizer if missing
#     if not os.path.exists(vec_output):
#         with st.spinner("Downloading text vectorizer from cloud..."):
#             url = 'https://drive.google.com/file/d/1QHiityuQD78RrMoTf5RESsGDa-QfpPNv'
#             gdown.download(url, vec_output, quiet=True)

#     # Download Stacking Model if missing
#     if not os.path.exists(model_output):
#         with st.spinner("Downloading Stacking Classifier model (390MB)... Please wait."):
#             url = 'https://drive.google.com/file/d/19bGiKPG0M3Pcy-ca0pV-kqGAeebmDBtM'
#             gdown.download(url, model_output, quiet=True)

#     # Load the downloaded pickle files
#     try:
#         with open(vec_output, 'rb') as f:
#             tfidf = pickle.load(f)
#         with open(model_output, 'rb') as f:
#             model = pickle.load(f)
#         return tfidf, model
#     except Exception as e:
#         st.error(f"Error reading model binaries: {e}")
#         return None, None

# # Initialize resources
# load_nltk_resources()
# ps = PorterStemmer()
# stop_words = set(stopwords.words('english'))
# punctuation = set(string.punctuation)
# custom_remove = {'subject'}

# # Fetch models
# tfidf, model = download_and_load_models()
# if tfidf is None or model is None:
#     st.warning("⚠️ Application is missing core classification models. Check your Google Drive links.")
#     st.stop()

# # Text pre-processing logic
# def transform_text(text):
#     text = text.lower()
#     tokens = nltk.word_tokenize(text)
#     transformed_tokens = [
#         ps.stem(token) for token in tokens 
#         if token.isalnum() and token not in stop_words and token not in punctuation and token not in custom_remove
#     ]
#     return " ".join(transformed_tokens)

# # User Interface
# st.title("📧 Email Spam Classifier")
# st.write("Determine whether an incoming message is a safe email (Ham) or a malicious message (Spam).")

# input_sms = st.text_area("Enter the message content below:", height=150)

# if st.button('Predict / Classify', type="primary"):
#     if not input_sms.strip():
#         st.warning("Please enter a message to classify.")
#     else:
#         try:
#             # 1. Preprocess
#             transformed_sms = transform_text(input_sms)
#             # 2. Vectorize
#             vector_input = tfidf.transform([transformed_sms])
#             # 3. Predict
#             result = model.predict(vector_input.toarray())[0]
#             # 4. Display result
#             if result == 1:
#                 st.error("🚨 **SPAM DETECTED**")
#             else:
#                 st.success("✅ **NOT SPAM (HAM)**")
#         except Exception as e:
#             st.error(f"An error occurred during verification: {e}")
