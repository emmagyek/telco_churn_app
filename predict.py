import streamlit as st
import pickle 
import pandas as pd
import joblib


# load the pipeline
@st.cache_resource
def load_lr_pipeline():
    with(open('models/logistic_regression_pipeline.pkl', 'rb') as file): 
        return joblib.load(file)                   


@st.cache_resource
def load_rf_pipeline():
    with(open('models/random_forest_pipeline.pkl', 'rb') as file): 
        return joblib.load(file)                   


# add your saved models into the folder 'models' 
def load_model(filename):
        with open(filename, mode='rb') as file:
            return joblib.load(file)
        

def predict_page():
    st.sidebar.title('Prediction Page')
    st.sidebar.write('Predict whether a customer will churn or not')


    pipeline = load_lr_pipeline()


    # load models
    '''
    models_path = {
        'Logistic Regression': 'models/logistic_regression_model.pkl', 
        'Decision Tree': 'models/decision_tree_model.pkl',
        'Random Forest': 'models/random_forest_model.pkl'
    }
    '''
    models_path = {
         'Random Forest': 'models/random_forest_pipeline.pkl',
         'Logistic Regression':'models/logistic_regression_pipeline.pkl'
    }
     
    model_choice = st.selectbox(label='Select a model of your choice', options=list(models_path.keys()))
    model = load_model(models_path[model_choice])

    if model is None:
        st.error('Failed to load model')
        return    


    # check the model type
    st.write(f'Loaded model type: {type(model)}')

    # single prediction
    st.subheader(body='Single Customer Prediction')
    gender = st.selectbox("Gender", ['Male', 'Female'])
    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    partner = st.selectbox("Partner", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    
    # predict for a single customer
    if st.button('Predict Single'):
         
         # create a dataframe for the single data
         data = pd.DataFrame(
        {
         'gender': [gender],
         'SeniorCitizen': [senior_citizen],
         'Partner': [partner],
         'Dependents': [dependents],
         'tenure': [tenure],
         'PhoneService': [phone_service],
         'MultipleLines': [multiple_lines],
         'InternetService': [internet_service],
         'OnlineSecurity': [online_security],
         'OnlineBackup': [online_backup],
         'DeviceProtection': [device_protection],
         'TechSupport': [tech_support],
         'StreamingTV': [streaming_tv],
         'StreamingMovies': [streaming_movies],
         'Contract': [contract],
         'PaperlessBilling': [paperless_billing],
         'PaymentMethod': [payment_method],
         'MonthlyCharges': [monthly_charges],
         'TotalCharges': [total_charges]
        }
         )

         # proces to the pipeline
         prediction = pipeline.predict(data)
         probability = pipeline.predict_proba(data)[0][1]*100


         # display results
         st.write(f"Single Prediction: {'Churn' if prediction == 1 else 'Not Churned'}")
         st.write(f"Probability of Churn: {probability: .2f}%")

         st.write(f"Pipeline type: {type(pipeline)}")

    
    # Bulk prediction
    st.header('Bulk Prediction')
    st.write('Upload a CSV file with customer data')

    uploaded_file = st.file_uploader('Choose the file to upload', type='csv')
    if uploaded_file is not None:
         try:
              bulk_data = pd.read_csv(uploaded_file)
              st.write('Data Preview', bulk_data.head())

              # required columns
              required_columns = [
                                    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
                                    'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
                                    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                    'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'
                                 ]

              if all(col in bulk_data.columns for col in required_columns):

                   bulk_predictions = pipeline.predict(bulk_data)
                   bulk_probabilities = pipeline.predict_proba(bulk_data)[:,1]*100 

                   # display results
                   bulk_results = bulk_data.copy()
                   bulk_results['Predictions'] = ['Churn' if pred== 1 else 'Not Churn' for pred in bulk_predictions]
                   bulk_results['Churn Probability'] = bulk_probabilities 

                   # display results
                   st.write('Bulk Prediction Results:')
                   st.dataframe(bulk_results)
                   
                   # save results
                   result_file = 'data.predictions_made.csv'
                   bulk_results.to_csv(result_file, index=False)
                   st.success(f'Results saved successfully to {result_file}')
              else:
                   st.error('Uploaded CSV file do not have the same columns')
                   
         except Exception as e:
              st.error(f'Error during loading')    


# run the predict page
if __name__ == '__main__':
     predict_page()