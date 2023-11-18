import streamlit as st
import pickle
import numpy as np
import pandas as pd

from utils.utils import prepare_for_test

with open('model/model.pkl','rb') as file:
            model = pickle.load(file)

def main():
    st.title('Cancer Surivival Prediction')
    
    Age = st.number_input("Age")
    Gender =  st.selectbox('Gender',['Male', 'Female'])
    Protein1 = st.number_input('Protein1')
    Protein2 = st.number_input('Protein2')
    Protein3 = st.number_input('Protein3')
    Protein4 = st.number_input('Protein4')
    Tumour_Stage = st.selectbox('Tumor_stage',['II', 'I', 'III'])
    Histology = st.selectbox('Histology',['Infiltrating Ductal Carcinoma', 'Infiltrating Lobular Carcinoma','Mucinous Carcinoma'])
    HER2_status = st.selectbox('HER2_status',['Negative', 'Positive'])
    Surgery_type = st.selectbox('Surgery_type',['Other', 'Lumpectomy', 'Modified Radical Mastectomy','Simple Mastectomy'])
    
    st.markdown(
    """ 
    #### Problem Statement 
     The objective here is to predict the Breast Cancer Survival Rate for a given order based on features like Age, Gender, Protein1,2,3,4 etc...
     """
    )
    survival_labels = {0: 'negative', 1: 'positive'}

    if st.button("Predict"):
        data = pd.DataFrame({
            'Age':[Age],
            'Gender':[Gender],
            'Protein1':[Protein1],
            'Protein2':[Protein2],
            'Protein3':[Protein3],
            'Protein4':[Protein4],
            'Tumour_Stage':[Tumour_Stage],
            'Histology':[Histology],
            'HER2_status':[HER2_status],
            'Surgery_type':[Surgery_type]
        })
        processed_data = prepare_for_test(data)
        
        prediction = model.predict(processed_data)
        
        st.success(f"The survival rate of patient is {survival_labels[prediction]} ")
    
if __name__ == "__main__":
    main()
    
    