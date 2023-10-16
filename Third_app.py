
import joblib
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.svm import SVC

try:
    Model = joblib.load("Third_Group.pkl")
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")


Model = joblib.load("Third_Group.pkl")
Inputs = joblib.load("inputs.pkl")

def prediction(gender, SeniorCitizen, Partner, Dependents, tenure,
       PhoneService, MultipleLines, InternetService, OnlineSecurity,
       OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
       StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
       MonthlyCharges, TotalCharges):
    df = pd.DataFrame(columns=Inputs)
    
    df.at[0, "gender"] = gender
    df.at[0, "SeniorCitizen"] = SeniorCitizen
    df.at[0, "Partner"] = Partner
    df.at[0, "Dependents"] = Dependents
    df.at[0, "tenure"] = tenure
    df.at[0, "PhoneService"] = PhoneService
    df.at[0, "MultipleLines"] = MultipleLines
    df.at[0, "InternetService"] = InternetService
    df.at[0, "OnlineSecurity"] = OnlineSecurity
    df.at[0, "OnlineBackup"] = OnlineBackup
    df.at[0, "DeviceProtection"] = DeviceProtection
    df.at[0, "TechSupport"] = TechSupport
    df.at[0, "StreamingTV"] = StreamingTV
    df.at[0, "StreamingMovies"] = StreamingMovies
    df.at[0, "Contract"] = Contract
    df.at[0, "PaperlessBilling"] = PaperlessBilling
    df.at[0, "PaymentMethod"] = PaymentMethod
    df.at[0, "MonthlyCharges"] = MonthlyCharges
    df.at[0, "TotalCharges"] = TotalCharges
    
    result = Model.predict(df)[0]
    return result

def main():
    st.image('https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png')
    st.title("Telco Customer Churn-Retention")
    gender = st.selectbox("gender",['Female', 'Male'])
    SeniorCitizen= st.selectbox("SeniorCitizen",[0, 1])
    Partner = st.selectbox("Partner",['Yes', 'No'])
    Dependents = st.selectbox("Dependents",['No', 'Yes'])
    tenure = st.slider("tenure", min_value=1, max_value=72, value=0, step=1)
    PhoneService = st.selectbox("PhoneService",['No', 'Yes'])
    MultipleLines = st.selectbox("MultipleLines",['No phone service', 'No', 'Yes'])
    InternetService = st.selectbox("InternetService",['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.selectbox("OnlineSecurity",['No', 'Yes', 'No internet service'])
    OnlineBackup = st.selectbox("OnlineBackup",['Yes', 'No', 'No internet service'])
    DeviceProtection = st.selectbox("DeviceProtection",['No', 'Yes', 'No internet service'])
    TechSupport = st.selectbox("TechSupport",['No', 'Yes', 'No internet service'])
    StreamingTV = st.selectbox("StreamingTV",['No', 'Yes', 'No internet service'])
    StreamingMovies = st.selectbox("StreamingMovies",['No', 'Yes', 'No internet service'])
    Contract = st.selectbox("Contract",['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.selectbox("PaperlessBilling",['Yes', 'No'])
    PaymentMethod = st.selectbox("PaymentMethod",['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])
     
    MonthlyCharges = st.slider("MonthlyCharges", min_value=18.25, max_value=118.75, value=68.5, step=1.0)
    TotalCharges = st.slider("TotalCharges", min_value=18.8, max_value=8684.8, value=68.5, step=1.0)
    
    if st.button("Predict"):
        result = prediction(gender, SeniorCitizen, Partner, Dependents, tenure,
       PhoneService, MultipleLines, InternetService, OnlineSecurity,
       OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
       StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
       MonthlyCharges, TotalCharges)
        list_result = ["Not Churn" , "Churn"]
        st.text(f"Your Customer is {list_result[result]}")

if __name__ == '__main__':
    main()
