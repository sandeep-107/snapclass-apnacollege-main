import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):

    st.write("Enter the details of new subject")

    sub_id = st.text_input(
        "Subject Code",
        placeholder="CS101"
    )

    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science"
    )

    sub_section = st.text_input(
        "Section",
        placeholder="A"
    )

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "Create Subject Now",
            type="primary",
            use_container_width=True
        ):

            if sub_id and sub_name and sub_section:

                try:
                    create_subject(
                        sub_id,
                        sub_name,
                        sub_section,
                        teacher_id
                    )

                    st.toast("Subject Created Successfully!")
                    st.session_state["show_create_subject_dialog"] = False
                    st.rerun()

                except Exception as e:
                    st.error(f"Error: {str(e)}")

            else:
                st.warning("Please fill all fields")

    with c2:
        if st.button(
            "Cancel",
            use_container_width=True
        ):
            st.session_state["show_create_subject_dialog"] = False
            st.rerun()
