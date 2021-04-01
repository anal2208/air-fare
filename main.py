import streamlit as st

st.header("Airface Prediction")

original_list = ['Select Item','Air India','Indigo','kingfisher']
result = st.selectbox('select youe favourite item',original_list)
st.write(f'You select: {result}')

col1, col2 = st.beta_columns(2)

dict_src = {'Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai'}
src = col1.radio('Source', list(dict_src))

dict_desti = {'Banglore', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata'}
desti = col2.radio('Destination', list(dict_desti))

dict_add_info = {'1 Long layover', '1 Short layover', '2 Long layover', 'Business class',
                 'Change airports', 'In-flight meal not included', 'No Info',
                 'No check-in baggage included', 'No info', 'Red-eye flight'}
add_info = st.selectbox('Additional information', list(dict_add_info))

full_date = st.date_input("Date of journey")
date = int(full_date.strftime("%d"))
month = int(full_date.strftime("%m"))

arr_hour = st.slider('Arrival Hour', min_value=0, max_value=23)

arr_min = st.slider('Arrival Minute', min_value=0, max_value=59)

dep_hour = st.slider('Departure Hour', min_value=0, max_value=23)

dep_min = st.slider('Departure Minute', min_value=0, max_value=59)

routes = {'AMD ', 'ATQ ', 'BBI ', 'BDQ ', 'BHO ', 'BLR', 'BLR ', 'BOM '}

rou1 = st.selectbox('Route 1', list(routes))
rou2 = st.selectbox('Route 2', list(routes))
rou3 = st.selectbox('Route 3', list(routes))
rou4 = st.selectbox('Route 4', list(routes))
rou5 = st.selectbox('Route 5', list(routes))
