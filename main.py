import streamlit as st
import pandas as pd

data = {
  'ser1':[1,2,3,4],
  'ser2':[10,20,30,40]
}

df=pd.DataFrame(data)

st.title("First streamlit app")
st.subheader("Introducing streamlit in automate everything with python")
st.write("""This is my first web app

enjoy it!
""")
st.write(df)
st.line_chart(df)
myslider=st.slider("Celsius")
st.write(myslider, "in Celsius is in Fahrenheit is",myslider*9/5+32)