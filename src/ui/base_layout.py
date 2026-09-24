import streamlit as st


def style_background_home():

    st.markdown("""
    <style>

    .stApp{
        background:#5865F2 !important;
    }

    div[data-testid="stColumn"]{
        background-color:#E0E3FF20;
        padding:2rem;
        border-radius:20px;
    }

    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
    <style>

    .stApp{
        background:#E0E3FF !important;
    }

    </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100;300;400;500;600;700&display=swap');

    /* Hide Top Bar of Streamlit */

    #MainMenu,
    #footer,
    header {
        visibility: hidden;
    }

    .block-container{
        padding-top:1rem;
        max-width:1000px;
    }

    /* Main Title */
    h1{
        font-family:'Climate Crisis', sans-serif !important;
        font-size:2.5rem !important;
        line-height:0.8 !important;
        margin:0 !important;
    }

    /* Streamlit Headers Only */
    div[data-testid="stMarkdownContainer"] h2{
        font-family:'Outfit', sans-serif !important;
        color:#5865F2 !important;
        font-weight:700 !important;
    }

    div[data-testid="stMarkdownContainer"] h3{
        font-family:'Outfit', sans-serif !important;
        font-weight:600 !important;
    }

    /* Text Inputs */

    .stTextInput input{
        border-radius:12px !important;
        padding:10px !important;
        background:#F5F5F5 !important;
        color:#333333 !important;
        border:none !important;
    }

    .stTextInput input::placeholder{
        color:#888888 !important;
        opacity:1 !important;
    }

    .stTextInput div[data-baseweb="input"]{
        background:#F5F5F5 !important;
        border-radius:12px !important;
    }

    label{
        color:#333333 !important;
        font-weight:600 !important;
    }

    /* Buttons */

    .stButton > button{
        width:100%;
        border-radius:15px;
        background:#EB459E;
        color:white;
        border:none;
        padding:12px;
        font-weight:bold;
        transition:0.3s;
    }

    .stButton > button:hover{
        transform:scale(1.03);
    }

    /* Dashboard Tabs */

    .stButton button[kind="primary"]{
        background:#5865F2 !important;
        color:white !important;
        border:none !important;
        border-radius:20px !important;
    }

    .stButton button[kind="tertiary"]{
        background:black !important;
        color:white !important;
        border:none !important;
        border-radius:20px !important;
    }

    </style>
    """, unsafe_allow_html=True)