import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import (
    style_base_layout,
    style_background_home
)


def home_screen():

    style_background_home()
    style_base_layout()

    header_home()

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # STUDENT
    with col1:

        st.markdown(
            "<h3>I'm Student</h3>",
            unsafe_allow_html=True
        )

        st.image(
            "https://static.vecteezy.com/system/resources/thumbnails/007/469/004/small/graduated-student-in-simple-flat-personal-profile-icon-or-symbol-people-concept-illustration-vector.jpg",
            use_container_width=True
        )

        if st.button(
            "↗ Student Portal",
            key="student_btn"
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    # TEACHER
    with col2:

        st.markdown(
            "<h3>I'm Teacher</h3>",
            unsafe_allow_html=True
        )

        st.image(
            "https://img.magnific.com/premium-vector/vector-logo-illustration-teacher-mascot-cartoon-style_116762-8535.jpg",
            use_container_width=True
        )

        if st.button(
            "↗ Teacher Portal",
            key="teacher_btn"
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    footer_home()