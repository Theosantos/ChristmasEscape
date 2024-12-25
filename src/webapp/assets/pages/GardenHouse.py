import time
import streamlit as st
from config import Image

def write():
    st.write("## Épreuve d'Enigma")
    st.write("De : Enigma")
    st.write("A : Mamie")
    st.write("---")
    st.image(Image.GARDENING)
    question = "Recoud les mots croisés et utilise les numéros pour trouver le mot caché :"
    answer = "mini maison"
    

    st.write(question)
    user_answer = st.text_input("Réponse :").lower()
    if user_answer == answer:
        st.balloons()
        st.success("Bravo pour la bonne réponse !")
        with st.spinner():
            time.sleep(5)
        st.write("Désolé pour la photo, le cadeau n'arrivera que Vendredi ...")
        st.write("-- Enigma ...")
        st.write(Image.GARDEN_HOUSE)
        st.image(Image.GARDEN_HOUSE, "A small garden house", width=600)
        st.write("*Petite serre à monter ensemble !*")

# On lance la fonction d'écriture de la page 
if __name__ == "__main__":
    write()