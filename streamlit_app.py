import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.write ("Bienvenue sur mon jeu de données Iris ")

long_petal = st.sidebar.slider("longueur du petal ",0.0,10.0)
larg_petal = st.sidebar.slider("largeur du petal ",0.0,10.0)
long_sepal = st.sidebar.slider("longueur du sepal ",0.0,10.0)
larg_sepal = st.sidebar.slider("largeur du sepal ",0.0,10.0)



if st.sidebar.button("predict",type="primary"):
  modele = joblib.load("iris_modele.pk1")
  normalise = joblib.load("normaliser_data.pk1")
  #convertir mes données recupérer de l'utilisateur en tableau
features = np.array([long_sepal,larg_sepal,long_petal,larg_petal])
#ajout des titre de colonnes
X = pd.DataFrame(features,columns=["SepalLength","SepalWidth","PetalLength","PetalWidth"])
#on normalise les données que le user a entré 
