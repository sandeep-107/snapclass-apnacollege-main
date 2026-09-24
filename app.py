import streamlit as st

from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.screens.home_screen import home_screen
from src.ui import base_layout
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapeClass - Making Attendance faster using AI',
        page_icon="https://pbs.twimg.com/profile_images/2068675522339717120/sYFAwBNP_400x400.jpg"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case _:
            home_screen()

    join_code = st.query_params.get("join-code")

    if join_code:

        if st.session_state.get("login_type") != "student":
            st.session_state.login_type = "student"
            st.rerun()

        if (
            st.session_state.get("is_logged_in")
            and st.session_state.get("user_role") == "student"
        ):
            auto_enroll_dialog(join_code)

if __name__ == "__main__":
    main()