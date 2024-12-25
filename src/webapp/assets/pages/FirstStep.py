import streamlit as st
from config import FakeSecrets, Steps, Clues

def password_game():
    if Steps.FIRST_STEP not in st.session_state:
        password = st.text_input("What is the password")
        if password == FakeSecrets.CLOSEPASSWORD:
            st.info("Did I ask for a french answer ?")
        elif password == FakeSecrets.MAINPASSWORD:
            st.balloons()
            st.write("Congrats on finding the password")
            st.session_state[Steps.FIRST_STEP] = "Done"

def write():
    st.write("## Introduction ")
    st.write("Welcome to this sick game of having to think to figure out what you won this year ...")
    password_game()
    if Steps.FIRST_STEP in st.session_state:
        st.write("First step done !")

        st.write("Insert clue code to know what to do next")
        clue_code = st.text_input("Clue code")
        if clue_code in Clues.CLUES_LIST and clue_code not in st.session_state:
            st.write("Good Job, you found a new clue")
            st.session_state[clue_code] = "Found"


if __name__ == "__main__":
    write()