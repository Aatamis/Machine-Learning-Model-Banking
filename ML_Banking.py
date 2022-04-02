import pickle
import numpy as np
import streamlit as st
import sklearn as sk

#model = pickle.load(open(r'C:\Users\hp\OneDrive\Documents\My First Machine Learning Model\Python Model\banking_churn.csv','rb'))
model = pickle.load(open('model_pkl','rb'))

#df = (r'C:\Users\hp\OneDrive\Documents\My First Machine Learning Model\Python Model\banking_churn.csv','rb')
#model = df


html_temp ="""
<div style ="background-color:#550A35 ;padding:10px">
<h2 style="color:white;text-align:center;">Bank Churn Prediction App</h2>
</div>
"""

st.markdown(html_temp,unsafe_allow_html=True)
CreditScore =st.text_input("Credit Score", placeholder="Type Score")
Geography =st.text_input("Geography", placeholder="France: 1, Spain: 2, Germany: 3")
Gender =st.text_input("Gender",placeholder="For Male, type 1, For Female type 2")
Age =st.text_input("Age",placeholder="Type Age")
Tenure =st.text_input("Tenure",placeholder="Type Tenure")
Balance =st.text_input("Balance",placeholder="Type Balance")
NumOfProducts =st.text_input("Number of Products",placeholder="Type the number of products here")
HasCrCard =st.text_input("Has a Credit Card",placeholder="Type 1 for 'Yes', 0 for 'No'")
IsActiveMember =st.text_input("Are they an Active Member?",placeholder="Type 1 for 'Yes', 0 for 'No'")
EstimatedSalary =st.text_input("EstimatedSalary",placeholder="Type Estimated Salary")


#prediction
if st.button('Predict'):
    makeprediction = model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,]])
    output=round(makeprediction[0],2)
    st.success('Customer is not likely to leave! {}'.format(output))

else:
    st.write('Customer is a high risk case! Take Action!')





