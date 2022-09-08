import streamlit as st
import pickle
import pandas as pd
from flaml import AutoML
import numpy as np
pipe=pickle.load(open('automl.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
load=pickle.load(open(r"D:\DOC\New folder\automl.sav",'rb'))






def GoalsPredictor(input_data):
    input_data_asarray=np.asarray(input_data)
    input_reshped=input_data_asarray.reshape(1,-1)
    Prediction=load.predict(input_reshped)
    print(Prediction)
    
    if (Prediction[0]==0):
        return "Predicted Goals are 0-3"
    elif (Prediction[0]==1):
        return "Predicted Goals are 3-6"
    else:
        return "Predicted Goals are 3-6"
 
    
def main():
    st.title("Football Goals Predictor")
    team1=st.selectbox('team1', df.team1.unique())
    team2=st.selectbox('team2', df.team2.unique())
    stadium=st.selectbox('stadium', df.stadium.unique())
    temp=st.selectbox("Temperature (°C)",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42])
    
    
    
    

    if st.button("Predict Goals"):
        input_data=[team1,team2,stadium,temp]

        input_data_asarray=np.asarray(input_data)
        input_reshped=input_data_asarray.reshape(1,-1)
        Prediction=load.predict(input_reshped)
        if (Prediction==0):
             Goals="Predicted Goals are 0-3"
        elif (Prediction==1):
             Goals="Predicted Goals are 3-6"
        else:
             Goals="Predicted Goals are 3-6"
        
    st.title(Goals)
        
    






if __name__=='__main__':
    main()
    

