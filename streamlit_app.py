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
    st.title (f"Bienvenue sur la page { selected}")
if selected=="AED": 
    st.title (f"Bienvenue sur la page de l'analyse exploratoire des données")
    st.header("Application AED")
    st.subheader("Notre jeu de données")
    if st.checkbox("voir les fleurs"):
        #les images des fleurs 
        st.image("iris_setosa.jpg")
        st.image("iris_versicolor.jpg")
        #st.image("iris_viginica.jpg")
    if st.checkbox("afficher jeu de données"):
        st.text("Affichage du jeu de données")    
        # jeu de données 
        jeu_donnees = 'iris.csv'
        def explorer_donnees(dataset):
            donnees = pd.read_csv(dataset)  # Charger les données
            return donnees
        donnees = explorer_donnees(jeu_donnees)
        if st.checkbox("image des données"):
            
            if donnees is not None:
                st.write(donnees)
        #Affichage des graphes 
        if st.checkbox("Diagramme circulaire"):        
if selected == "Predictions":
    st.title(f"Bienvenue sur ma page de {selected}")
    
    # Récupérer les données entrées par l'utilisateur dans les variables
    long_petal = st.slider("Longueur du pétale", 0.0, 10.0)
    larg_petal = st.slider("Largeur du pétale", 0.0, 10.0)
    long_sepal = st.slider("Longueur du sépale", 0.0, 10.0)
    larg_sepal = st.slider("Largeur du sépale", 0.0, 10.0)

    # Dès que je clique sur le bouton
    if st.button("Prédire", type="primary"):
        # Charger mon modèle et le fichier de normalisation des données
        modele = joblib.load("iris_modele.pk1")
        normalise = joblib.load("normaliser_data.pk1")

        # Convertir les données récupérées de l'utilisateur en tableau
        features = np.array([[long_sepal, larg_sepal, long_petal, larg_petal]])

        # Ajouter les titres des colonnes et constituer le DataFrame
        X = pd.DataFrame(features, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])

        # Normaliser les données que l'utilisateur a entrées
        X_transform = normalise.transform(X)

        # Faire la prédiction avec le modèle
        prediction = modele.predict(X_transform)

        # Récupérer juste le nom de la fleur et afficher le résultat
        reponse_modele = prediction[0]
        st.write("Votre fleur : ", reponse_modele)

