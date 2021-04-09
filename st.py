# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:29:39 2021

@author: shash
"""

#Libraries=====================================================================
import streamlit as st
import pickle
import datetime
import xlrd
import pandas as pd
#import numpy as np
#from math import sqrt

#from sklearn.preprocessing import LabelEncoder
#from sklearn.model_selection import train_test_split
#==============================================================================

#Reading the data==============================================================
train_df = pd.read_excel("Data_Train.xlsx")
test_df = pd.read_excel("Test_set.xlsx")
df = train_df.append(test_df)

df_Price = pd.read_excel("Data_Price.xlsx")
#==============================================================================

#Preprocessing the data========================================================

dict_airline = {'Air Asia': 0, 'Air India': 1, 'GoAir': 2, 'IndiGo': 3, 'Jet Airways': 4,
                'Jet Airways Business': 5, 'Multiple carriers': 6, 'Multiple carriers Premium economy': 7,
                'SpiceJet': 8, 'Trujet': 9, 'Vistara': 10, 'Vistara Premium economy': 11}

dict_src = {'Banglore': 0, 'Chennai': 1, 'Delhi': 2, 'Kolkata': 3, 'Mumbai': 4}

dict_desti = {'Banglore': 0, 'Cochin': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4}

dict_add_info = {'1 Long layover': 0, '1 Short layover': 1, '2 Long layover': 2, 'Business class': 3,
                 'Change airports': 4, 'In-flight meal not included': 5, 'No Info': 6,
                 'No check-in baggage included': 7, 'No info': 8, 'Red-eye flight': 9}

routes = {'AMD ': 28, 'ATQ ': 13, 'BBI ': 2, 'BDQ ': 12, 'BHO ': 41, 'BLR': 4, 'BLR ': 44, 'BOM ': 18,
          'CCU': 36, 'CCU ': 38, 'COK': 25, 'COK ': 30, 'DED ': 19, 'DEL': 27, 'DEL ': 15, 'GAU ': 22,
          'GOI ': 33, 'GWL ': 20, 'HBX ': 45, 'HYD': 29, 'HYD ': 0, 'IDR ': 26, 'IMF ': 47, 'ISK ': 5,
          'IXA ': 7, 'IXB ': 34, 'IXC ': 37, 'IXR ': 31, 'IXU ': 3, 'IXZ ': 11, 'JAI ': 24, 'JDH ': 16,
          'JLR ': 21, 'KNU ': 46, 'LKO ': 42, 'MAA ': 9, 'NAG ': 8, 'NDC ': 1, 'None': 6, 'PAT ': 48,
          'PNQ ': 10, 'RPR ': 43, 'STV ': 23, 'TIR ': 35, 'TRV ': 39, 'UDR ': 32, 'VGA ': 14, 'VNS ': 40,
          'VTZ ': 17}
#==============================================================================


#ML Model======================================================================
model = pickle.load(open('xgb_model.sav', 'rb'))
#==============================================================================


#GUI===========================================================================
st.title('Airfare PPrediction')

# airline = st.selectbox('Select airline', list(dict_airline.keys()), index = list(dict_airline.keys()).index('Jet Airways'))
col1, col2 = st.beta_columns(2)
src = col1.radio('Source', list(dict_src.keys()))
desti = col2.radio('Destination', list(dict_desti.keys()))
# add_info = st.selectbox('Additional information', list(dict_add_info.keys()), index = list(dict_add_info.keys()).index('No info'))
full_date = st.date_input("Date of journey")
date = int(full_date.strftime("%d"))
month = int(full_date.strftime("%m"))
#year = int(full_date.strftime("%y))
# arr_hour = st.slider('Arrival Hour', min_value=0, max_value=23, value=12) 
# arr_min = st.slider('Arrival Minute', min_value=0, max_value=59, value=0)
# dep_hour = st.slider('Departure Hour', min_value=0, max_value=23, value=10)
# dep_min = st.slider('Departure Minute', min_value=0, max_value=59, value=0)
rou1 = st.selectbox('Route 1', list(routes.keys()))
rou2 = st.selectbox('Route 2', list(routes.keys()))
# rou3 = st.selectbox('Route 3', list(routes.keys()), index = list(routes.keys()).index('None'))
# rou4 = st.selectbox('Route 4', list(routes.keys()), index = list(routes.keys()).index('None'))
# rou5 = st.selectbox('Route 5', list(routes.keys()), index = list(routes.keys()).index('None'))


col = ['Airline', 'Source', 'Destination', 'Additional_Info', 'Date', 'Month',
       'Arrival_Hour', 'Arrival_Minute', 'Dep_Hour', 'Dep_Minute', 'Route_1',
       'Route_2', 'Route_3', 'Route_4', 'Route_5']

val = [[4, dict_src[src], dict_desti[desti], 8, date, month, 
        12, 0, 10, 0, routes[rou1], routes[rou2], 6, 6, 6]]

df_test = pd.DataFrame(val, columns =col)
predicted_fare = model.predict(df_test)

if src == desti:
    st.header("Fare is: 0")
else:
    st.header("Fare is: " + str(predicted_fare[0]))
    price = int(df_Price.loc[(df_Price['To'] == src) & (df_Price['From '] == desti)]['Per seat cost'])
    if predicted_fare[0] >= price:
        st.write("Profit per seat: ", predicted_fare[0]-price)
    else:
        st.write("Loss per seat: ", predicted_fare[0]-price)
        
        

#==============================================================================
