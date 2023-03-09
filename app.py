import streamlit as st

st.title(':red[Innomatics] Data app :sunglasses:')
st.snow()

st.header('Data science internship')

st.subheader('Feb 2023')

CODE= '''print('Hello world)'''
st.code( CODE, language='python')

button= st.button('Click me')
if button == True:
    st.subheader("you clicked me :cry:")
    st.balloons()