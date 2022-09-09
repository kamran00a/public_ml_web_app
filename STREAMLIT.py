import streamlit as st
import pickle
import pandas as pd
from sklearn.svm import SVC  
import numpy as np
#pipe=pickle.load(open('automl.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))



def GoalsPredictor(input_data):
    input_data_asarray=np.asarray(input_data)
    input_reshped=pd.DataFrame({'team1':[team1],'team2':[team2],'stadium':[stadium],'temp':[temp]})
    Prediction=pipe.predict(input_reshped)

    print(Prediction)

    if (Prediction==0):
         print("Predicted Goals are 0-2")
    elif (Prediction==1):
         print("Predicted Goals are 2-4")
    elif (Prediction==2):
        print("Predicted Goals are 4-6")
    else:
         print("Predicted Goals are 6-10")
 
    
def main():
    st.title("Football Goals Predictor")
    team1=st.selectbox('team1', sorted(df.team1.unique()))
    team2=st.selectbox('team2', sorted(df.team2.unique()))
    stadium=st.selectbox('stadium', sorted(df.stadium.unique()))
    temp=st.selectbox("Temperature (°C)",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42
                                          ])
    
    
    
    

    if st.button("Predict Goals"):
        input_data=[team1,team2,stadium,temp]
        
        input_data_asarray=np.asarray(input_data)
        input_reshped=pd.DataFrame({'team1':[team1],'team2':[team2],'stadium':[stadium],'temp':[temp]})
        Prediction=pipe.predict(input_reshped)

        print(Prediction)

        if (Prediction==0):
             Goals="Predicted Goals are 0-2"
        elif (Prediction==1):
             Goals="Predicted Goals are 2-4"
        elif (Prediction==2):
            Goals="Predicted Goals are 4-6"
        else:
             Goals="Predicted Goals are 6-10"
        
     
        
    st.title(Goals)           
    
if __name__=='__main__':
    main()
    



        
    








