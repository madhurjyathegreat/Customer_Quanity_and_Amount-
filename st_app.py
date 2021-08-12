import streamlit as st
import numpy as np
import pickle as pkl
import pandas as pd

color = st.color_picker('Pick A Color', '#00f900')
st.title("AI to Predict Customer Quantiy and Amount",color)
# getting the inputs:-

city = st.selectbox("Select the city",('Lucknow', 'Delhi', 'Kolkata', 'Chennai', 'Ludhiana', 'Thiruvananthapuram', 'Kanpur', 'Hyderabad', 'Bangalore', 'Ahmedabad', 'Mumbai', 'Surat'))

brand=st.selectbox("Select Brand Number",( 3, 10,  1,  2,  8,  4,  5,  7,  6,  9))

model=(st.text_input("Enter model"))

price=(st.text_input("Enter price"))

ram=(st.selectbox("Select RAM size",( 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26)))

internal_memory=(st.selectbox("Enter internal memory",( 1,    2, 1001,    3,    4,    5,    6)))



# trying date formatting
date = st.date_input("Enter the date")
day=pd.to_datetime(date).day
weekofyear=pd.to_datetime(date).weekofyear
dayofweek=pd.to_datetime(date).dayofweek
#st.markdown(d_try)


city_mapping={'Lucknow': 525,
 'Delhi': 387,
 'Kolkata': 230,
 'Chennai': 123,
 'Ludhiana': 61,
 'Thiruvananthapuram': 59,
 'Kanpur': 39,
 'Hyderabad': 12,
 'Bangalore': 8,
 'Ahmedabad': 6,
 'Mumbai': 3,
 'Surat': 1}



if city in city_mapping.keys():
    new_city = (city_mapping.get(city))



list1=[new_city,brand,model,price,ram,internal_memory,day,weekofyear,dayofweek]



new_list = [int(i) for i in list1]

new_list=np.array(new_list).reshape(1,-1)



loaded_model = pkl.load(open(r"C:\Users\91996\Desktop\ML\PredictiVu\final_model.pkl", 'rb'))

predicted_value=loaded_model.predict(new_list)



if(st.button("Predict the quantity and price ")):
  st.header("The Quantity that will be ordered is : "+str(int(predicted_value[0][0])))
  st.header("The Amount that will be ordered is : " + str(int(predicted_value[0][1])))






