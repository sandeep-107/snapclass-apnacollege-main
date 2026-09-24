import streamlit as st


def footer_home():

    logo_url = "https://logos-world.net/wp-content/uploads/2020/09/Google-Logo.png"

    st.markdown(
        f'<div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;"><span style="font-weight:bold; color:white; font-size:22px;">Created with ❤️ by</span><img src="{logo_url}" style="height:50px;" /></div>',
        unsafe_allow_html=True
    )


def footer_dashboard():

    logo_url = "https://logos-world.net/wp-content/uploads/2020/09/Google-Logo.png"

    st.markdown(
        f'<div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;"><span style="font-weight:bold; color:#5865F2; font-size:20px;">Created with ❤️ by</span><img src="{logo_url}" style="height:40px;" /></div>',
        unsafe_allow_html=True
    )
