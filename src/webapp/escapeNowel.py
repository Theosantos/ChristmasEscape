from config import Steps, Clues
import streamlit as st
from PIL import Image
import awesome_streamlit as ast
from assets.pages import FirstStep, CodeCracking, GardenHouse, HideAndSeek, WellDone



def get_pages():
    pages = {
        "🎓 1ere Etape": FirstStep
    }
    if Clues.FIRST_CLUE in st.session_state:
        pages["🧑‍💻 Code cracking"] = CodeCracking
    if Clues.THIRD_CLUE in st.session_state:
        pages["🌱 Enigma"] = GardenHouse
    if Clues.SECOND_CLUE in st.session_state:
        pages["🔎 Hide and Seek"] = HideAndSeek
    if Clues.LAST_CLUE in st.session_state: 
        pages[" Well Done !"] = WellDone
    return pages

def display_sidebar():
    pages = get_pages()
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Choisir la page", list(pages.keys()))
    page = pages[selection]
    st.sidebar.markdown("""---""")
    with st.sidebar:
        st.button("Check for new pages")
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    

    

def main():
    """Main function of the app"""
    display_sidebar()
    


if __name__ == "__main__":
    st.set_page_config(
        layout="wide", page_icon="🎁", page_title="OuEstMonKdo"
    )
    st.title('Where is my gift ???')
    main()