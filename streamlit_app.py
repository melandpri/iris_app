import streamlit as st
st.write ("Bienvenue sur mon jeu de données Iris ")

st.sidebar.slider("longueur du petal ",0.0,10.0)
st.sidebar.slider("largeur du petal ",0.0,10.0)
st.sidebar.slider("longueur du sepal ",0.0,10.0)
st.sidebar.slider("largeur du sepal ",0.0,10.0)



if st.sidebar.button("predict",type="primary"):
  st.write("result")
st.write("mon app")
