import streamlit as st
import pandas as pd

def data_page():
    st.title('Data Page')
    
    st.sidebar.title('Data Understanding')

    st.sidebar.write('This helps you to understand the data that you will use')

    columns_description = {
        "Gender": "Whether the customer is a male or a female",
        "SeniorCitizen": "Whether a customer is a senior citizen or not",
        "Partner": "Whether the customer has a partner or not (Yes, No)",
        "Dependents": "Whether the customer has dependents or not (Yes, No)",
        "Tenure": "Number of months the customer has stayed with the company",
        "Phone Service": "Whether the customer has a phone service or not (Yes, No)",
        "MultipleLines": "Whether the customer has multiple lines or not",
        "InternetService": "Customer's internet service provider (DSL, Fiber Optic, No)",
        "OnlineSecurity": "Whether the customer has online security or not (Yes, No, No Internet)",
        "OnlineBackup": "Whether the customer has online backup or not (Yes, No, No Internet)",
        "DeviceProtection": "Whether the customer has device protection or not (Yes, No, No Internet)",
        "TechSupport": "Whether the customer has tech support or not (Yes, No, No Internet)",
        "StreamingTV": "Whether the customer has streaming TV or not (Yes, No, No Internet)",
        "StreamingMovies": "Whether the customer has streaming movies or not (Yes, No, No Internet)",
        "Contract": "The contract term of the customer (Month-to-Month, One year, Two year)",
        "PaperlessBilling": "Whether the customer has paperless billing or not (Yes, No)",
        "Payment Method": "The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))",
        "MonthlyCharges": "The amount charged to the customer monthly",
        "TotalCharges": "The total amount charged to the customer",
        "Churn": "Whether the customer churned or not (Yes or No)"
    }

    col1, col2 = st.columns(2)

    with col1:
        selected_column = st.selectbox(
            'Select a column to see its description',
            # a list in this function becomes options that users can select from
            list(columns_description.keys()),
            key='columns_description_select')
        
    with col2:
        def filter_column(data):
            data_type = st.selectbox(label='Select Between Numerical and Categorical Columns', 
                                     options=['All', 'Numerical columns', 'Categorical columns'])
            
            if data_type == 'Numerical columns':
                data = data.select_dtypes(include=['number'])
            elif data_type == 'Categorical columns':
                data = data.select_dtypes(include=['object','category'])
            
            st.write(data)
            
    # add the path to the data set
    #dataset_path = "E:/Azubi/Phase 2\Week 4-6_Classification project/Main Project/trainset.csv"
    dataset_path = 'Data/trainset.csv'

    data = pd.read_csv(dataset_path)
    
    # Display the dataframe
    st.write('Dataset Overview')
    st.write(data)

    # call the filter column function
    filter_column(data)
