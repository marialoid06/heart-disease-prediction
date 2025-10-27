❤️ Heart Disease Prediction App
A user-friendly web application built with Streamlit and Scikit-learn to predict the risk of heart disease based on patient medical data.

📋 About The Project
This project aims to provide an intuitive interface for a heart disease prediction model. Users can input various medical parameters, and the application leverages a trained Logistic Regression model to provide a risk assessment in percentage terms, along with a qualitative interpretation (Low, Moderate, High Risk).

The model was trained on the publicly available Cleveland Clinic heart disease dataset.

✨ Features
Interactive and user-friendly web interface.

Input fields for all 13 key medical attributes.

Real-time prediction of heart disease risk percentage.

Clear, color-coded results with actionable advice.

Detailed explanations for each medical parameter.

🚀 How To Run This Project Locally
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.8 or higher

Git

Installation & Setup
Clone the repository:

git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
cd <YOUR_REPO_NAME>

Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Your browser should open with the application running!

acknowledgements
Dataset: Cleveland Clinic Heart Disease Dataset on Kaggle

Frameworks: Streamlit, Scikit-learn, Pandas