import streamlit as st
st.write ("Bienvenue sur mon jeu de données Iris ")

st.sidebar
st.slider("longueur du petal ",0.0,10.0)

if st.button("mon_bouton",type="primary"):
  st.write("result")
st.write("mon app")
