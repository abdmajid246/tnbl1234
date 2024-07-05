import streamlit as st
import pandas as pd
import pickle #to ?
from PIL import Image



df = pd.read_csv('electricity_usage.csv')
st.dataframe(df)

Image.open('tnb.png').convert('RGB').save('tnb.png')
im = Image.open("tnb.png")
st.image(im,width=300,caption ="TNB Logo")


col1,col2 =st.columns(2)

with col1:

 
    st.info("This is column one")
    
    df_city1= df.groupby("City")['MonthlyHours'].sum().reset_index()

    st.bar_chart(df_city1, x="City",y="MonthlyHours")

    fan = st.slider("Number of Fan",5,20, value =10)
    fridge = st.slider("Number of Refrigerator",18,23,value=20)
    aircon = st.slider("Number of Aircon", 0,3,value =1)
   

with col2:


    st.success("This is column two")
    df_city2= df.groupby("City")['ElectricityBill'].sum().reset_index()

    st.bar_chart(df_city2, x="City",y="ElectricityBill")
    tv = st.slider("Number of TV", 5,20,value =3)
    hour = st.slider("Number of Hours",390,600,value=400)

model = pickle.load(open("LRmodel.pkl","rb"))

new_data = {'Fan':[fan],'Refrigerator':[fridge],'AirConditioner':[aircon],'Television':[tv],'MonthlyHours':[hour]}

pd.DataFrame.from_dict(new_data)

pred = model.predict(pd.DataFrame.from_dict(new_data))
pred = round(pred[0],2)

st.subheader('The Predicted Electricity Bill is ' + str(pred))