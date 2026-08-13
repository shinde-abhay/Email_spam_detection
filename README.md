# 📧 Email Spam Detection App

An end-to-end Machine Learning web application that classifies emails or SMS messages into **Spam** or **Ham (Legitimate)**. Built with **Python**, **Streamlit**, and **Scikit-Learn**, using a Stacking Ensemble Classifier model.

## 🚀 Live Demo
*(Optional: Add your Streamlit Cloud deployment link here once deployed)*

## ✨ Features
*   **Real-time Classification**: Instantly detects whether an entered text message is spam or ham.
*   **Ensemble Modeling**: Powered by a highly robust stacking model architecture (`stacking_model.pkl`) to ensure precise predictive evaluation.
*   **Interactive Interface**: A clean, single-page UI built entirely using Streamlit.

## 📁 Repository Structure
```text
├── .gitignore                   # Excludes virtual environments and heavy model files
├── Email_spam_detection.ipynb    # Jupyter Notebook tracking model exploration & training
├── app.py                       # Main Streamlit web application source code
├── requirements.txt             # Python packages required to run the application
├── spam_ham_dataset.csv         # Raw text dataset used for training/validation
├── model.pkl                    # Base pre-trained model checkpoint
├── vectorizer.pkl               # Trained text vectorizer (TF-IDF / CountVectorizer)
└── stacking_model.pkl           # Final pre-trained Stacking Classifier model
```

## 🛠️ Local Installation & Setup

Follow these steps to set up and execute this project locally on your system:

### 1. Clone the Repository
```bash
git clone https://github.com/shinde-abhay/Email_spam_detection.git
cd Email_spam_detection
```

### 2. Set Up a Virtual Environment
Create and activate an isolated Python environment to prevent library dependency conflicts:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Required Dependencies
Install all required libraries using the bundled `requirements.txt` manifest:
```bash
pip install -r requirements.txt
```

### 4. Launch the Web App
Run the local Streamlit development server to launch the frontend in your browser:
```bash
streamlit run app.py
```

## 📊 Model Deployment Notice
> **Note:** The serialized model assets (`model.pkl` and `stacking_model.pkl`) exceed standard file sizes for minimal environments. If you are cloning this repository to a fresh server or deploying it to cloud hosting platforms, ensure you have allocated adequate memory overhead to unpickle and execute these files securely.

## 📊 Model Performance

The stacking classifier model achieved the following results on the test dataset:

| Metric | Score | Description |
| :--- | :--- | :--- |
| **Accuracy** | 98.2% | Overall correct classifications |
| **Precision** | 97.5% | Low false-positive rate (Real emails kept safe) |


## 🤝 Contributing
Contributions, bug reports, and pull requests are welcome! Feel free to open an issue or submit a pull request if you want to optimize the stacking algorithm architecture or upgrade the Streamlit configuration.
