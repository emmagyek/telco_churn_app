import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dashboard_page():
    st.title('Dashboard Page')

    # load data
    data = pd.read_csv('Data/trainset.csv')

    st.header('Data Overview')
    st.write('Here is a quick summary of the data')
    st.dataframe(data.head())

    st.subheader('Churn Count')
    churn_count = data['Churn'].value_counts()
    st.bar_chart(data=churn_count)

    # Churn Rate Pie Chart
    st.subheader("Churn Rate")
    churn_counts = data['Churn'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(churn_counts, labels=['No Churn', 'Churn'], autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)
    
    # Tenure and Churn Histogram
    st.subheader("Tenure Distribution by Churn Status")
    fig, ax = plt.subplots()
    sns.histplot(data=data, x="tenure", hue="Churn", multiple="stack", ax=ax)
    st.pyplot(fig)

    # Monthly Charges Box Plot
    st.subheader("Monthly Charges by Churn Status")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x="Churn", y="MonthlyCharges", ax=ax)
    st.pyplot(fig)

    # Contract Type vs Churn Rate
    st.subheader("Churn Rate by Contract Type")
    contract_churn = pd.crosstab(data['Contract'], data['Churn'], normalize='index')  # Normalize by row for percentage
    contract_churn = contract_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots()
    contract_churn.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Contract Type')
    st.pyplot(fig)

     # Payment Method vs Churn
    st.subheader("Churn Rate by Payment Method")
    payment_churn = pd.crosstab(data['PaymentMethod'], data['Churn'], normalize='index')  # Normalize by row for percentage
    payment_churn = payment_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots()
    payment_churn.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Payment Method')
    st.pyplot(fig)