import streamlit as st
import time

from config import Steps, Image

def lettre(c):
    car = ord(c.upper())
    return car>64 and car<91

def decalage(c,k):
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""

def vigenere(message,cle,crypte):
    n = 0
    chiffre=''
    for c in message:
        if lettre(c):
            k = ord(cle[n%len(cle)])-65
            if crypte:
                chiffre += decalage(c,k)
            else:
                chiffre += decalage(c,-k)
            n+=1
        else:
            chiffre += c
    return chiffre


def code_cracking():
    instructions = "**Key tips**: Some people think that I am from there but I’m actually a neighbor of this place"
    sentence = "Congrats, I am not from Japan, but you will soon experience some of their culture"
    key = "japan"
    st.write(instructions)
    user_key = st.text_input("Key").lower()
    encoded = vigenere(sentence, key, True).title()
    st.write(f"**Encoded sentence**: {encoded}")
    if user_key != "":
        decoded = vigenere(encoded, user_key, False).title()
        st.write(f"**Decoded sentence**: {decoded}")

        if user_key == "china":
            st.info("I told you the answer is **not** the country I'm from")
        elif user_key == key:
            st.success("Congrats on finding the right key")
            st.balloons()
            st.session_state[Steps.SECOND_STEP] = "Done"
            with st.spinner("Gift loading"):
                time.sleep(5)
            with st.spinner("Oops, it's taking a while ..."):
                time.sleep(5)
            with st.spinner("Nah just kidding here you go"):
                time.sleep(5)
            st.image(Image.CUISINE)
            st.write("Gift is a meal in a fancy Japanese restaurant for Aya and Hugo with Theo")
        else:
            st.error("**Bad key**")


def write():
    st.write("## Code Cracking")
    st.write("The next sentence has been encrypted using a key that you must solve thanks to the your clue")
    code_cracking()
    st.write("---")


if __name__ == "__main__":
    write()