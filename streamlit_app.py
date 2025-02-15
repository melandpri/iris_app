import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from streamlit_option_menu import option_menu
from PIL import Image  
import os 


with st.sidebar: 
    selected=option_menu(
        menu_title=None,
        options=["Accueil" ,"AED","predictions"],
        icons=["house" , "bar-chart","activity"],
        menu_icon="cast",
        default_index=0,
    )
if selected=="Accueil": 
    st.title (f"Bienvenue sur la page accueil { selected}")
if selected=="AED": 
    st.title (f"Bienvenue sur la page de l'analyse exploratoire des données { selected}")
    st.header("Application AED")
    st.subheader("Notre jeu de données")
    
    if st.checkbox("voir les fleurs"):
        #les images des fleurs 
        st.image("iris_setosa.jpg")
        st.image("iris_versicolor.jpg")
        #st.image("iris_viginica.jpg")
   if st.checkbox("afficher jeu de données"):
       st.text("Affichage du jeu de données")
       #jeu de données 
        
       # Tester si Pandas peut ouvrir le fichier
       try:
           donnees = pd.read_excel('Iris.xlsx')
           print(donnees.head())  # Affiche les premières lignes du dataframe
       except Exception as e:
           print(f"Erreur : {e}")


        



              
if selected == "Predictions": 
    st.title (f"Bienvenue sur ma page de preditions  { selected}") 



#je recuperer les données entrer par l'utilisateur dans mes variables long_petal ....

long_petal = st.slider("longueur du petal ",0.0,10.0)
larg_petal = st.slider("largeur du petal ",0.0,10.0)
long_sepal = st.slider("longueur du sepal ",0.0,10.0)
larg_sepal = st.slider("largeur du sepal ",0.0,10.0)


#des que je clique sur le bouton 
if st.button("predict",type="primary"):
  #je charges mes mon modèle ,et le fichier qui normalisera les données recuperer de l'utilisateur
  modele = joblib.load("iris_modele.pk1")
  normalise = joblib.load("normaliser_data.pk1")
  #je convertis mes données recupérer de l'utilisateur en tableau
  features = np.array([[long_sepal,larg_sepal,long_petal,larg_petal]])
  #ajout des titre de colonnes,ici je cherche a recupérer mes données pour constituer mon dataframe 
  X =pd.DataFrame(features, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])
  #on normalise Ces données que le user a entré 
  X_transform = normalise.transform(X)
  #je predicte mes données 
  prediction = modele.predict(X_transform)
  #je recupère juste le nom de la fleur  et j affiche le résultat 
  reponse_modele = prediction[0]
  st.write("votre fleur: ",reponse_modele)
