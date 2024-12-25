import time
import streamlit as st
from config import FakeSecrets, Steps, Image


def write():
    st.write("## Congratulations")
    st.balloons()
    if True:
        st.write("Congrats for finishing every steps until now")
        st.write("To test your skills there will be two more tests in the days to come.")
        st.write("Come to me when you are ready")
        with st.spinner("Loading gift"):
            time.sleep(5)
        st.image(Image.FINAL_GIFTS, "Escape game tickets", width=600)
        st.write("Available for Aya, Hugo, Papa et Maman")

if __name__ == "__main__":
    write()