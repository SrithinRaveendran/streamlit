import pickle
import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from joblib import load
#model = load('C:/Users/SRITHIN RAVEENDRAN/Desktop/project2/cibil_Score.joblib','rb')
model=pickle.load(open('C:/Users/SRITHIN RAVEENDRAN/Desktop/for vscode/cibil_Score.pkl','rb'))
def main():
    st.title('CREDIT SCORE PREDICTION')
    enq_L3m = st.text_input('Enquiries in last 3 months')
    Other_TL = st.text_input('Count of other accounts')
    num_std_12mts = st.text_input('Number of standard Payments in last 12 months')
    time_since_recent_enq = st.text_input('Time since recent enquiry')
    max_recent_level_of_deliq = st.text_input('Maximum recent level of delinquency')
    recent_level_of_deliq = st.text_input('Recent level of delinquency')
    Age_Oldest_TL = st.text_input('Age of oldest opened account')
    num_std = st.text_input('Number of standard Payments')
    time_since_recent_payment = st.text_input('Time Since recent Payment made')
    Time_With_Curr_Empr = st.text_input('Time with current Employer')
    NETMONTHLYINCOME = st.text_input('Net Monthly Income')
    AGE= st.input_text('Age')
    num_times_delinquent =st.input_text('Number of times delinquent')
    pct_currentBal_all_TL = st.input_text('Percent current balance of all accounts')
    if st.button('Predict'):
        makeprediction=model.predict([[enq_L3m,Other_TL,num_std_12mts,time_since_recent_enq,max_recent_level_of_deliq,recent_level_of_deliq,
        Age_Oldest_TL,num_std,time_since_recent_payment,Time_With_Curr_Empr,NETMONTHLYINCOME,AGE,num_times_delinquent,pct_currentBal_all_TL]])
        output=round(makeprediction[0],2)
        st.success('Your Credit Score is{}'.format(output))
    if __name__=='__main__' :
        main()
