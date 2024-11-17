# telco_churn_app

Telco Churn Prediction App
📋 Overview
This Streamlit app predicts customer churn for a telecom company. It allows users to input customer data and uses machine learning models (Logistic Regression and Random Forest) to determine the likelihood of a customer churning. The app is designed to provide actionable insights to reduce churn rates and improve customer retention strategies.

🌟 Features
Interactive user interface for adding customer details.
Predicts churn probabilities using:
Logistic Regression
Random Forest Classifier
Allows switching between different models for predictions.
Displays detailed prediction results for better understanding.
Built with a focus on scalability and ease of use.
🚀 How to Use
Open the app in your browser (after deployment link is available).
Fill in the required customer details:
Gender, age, tenure, monthly charges, contract type, etc.
Select a machine learning model (Logistic Regression or Random Forest).
Click "Predict" to get the churn probability.
⚙️ Technical Details
Machine Learning Pipeline
The app is built on a robust ML pipeline:

Data Preprocessing: Cleans and transforms the Telco Churn dataset.
Models Used: Logistic Regression, Random Forest Classifier.

Technologies and Tools
Languages: Python
Libraries:
Streamlit (for the user interface)
Scikit-learn (for machine learning models)
Pandas & NumPy (for data handling)
Joblib (for model serialization)
Dataset: Telco Churn dataset
