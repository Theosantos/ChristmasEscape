import time
import streamlit as st

from config import Image


def write():
    st.write("Some gifts decided to play hide and seek, will you be able to find all of them ?")

    options = ["Mom", "Dad"]
    who = st.radio("Who are you ?", options=options)
    ready = st.checkbox("Ready to answer a difficult question ?")
    if ready:
        if who == "Mom": 
            question = "What is my favorite spice ? (French answer)"
            st.write(question)
            answer = "safran"
            user_answer = st.text_input("Answer:").lower()
            if user_answer == answer:
                st.success("Good job !")
                st.write("Here is the picture of your gift, good luck finding it :D ")
                st.image(Image.GIFT_MOM)


        if who == "Dad":
            answer = 54
            dad_question = "What is **7 x 8** ?"
            st.write(dad_question)
            user_answer = st.number_input("Answer:")
            if user_answer == answer:
                with st.spinner("Verifying answer"):
                    st.error("Wrong answer")
                    time.sleep(3)
                st.success("Nag i'm just messing with you, good job !")
                st.write("Here is the picture of your gift, good luck finding it :D ")
                st.image(Image.GIFT_DAD)

    # Pictures of hiden gifts
    return

# On lance la fonction d'écriture de la page 
if __name__ == "__main__":
    write()