import streamlit as st
import pandas as pd

from datetime import datetime

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase

from src.components.dialog_attendance_results import (
    show_attendance_result
)


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):

    # -----------------------------
    # Session State Init
    # -----------------------------
    if "voice_attendance_results" not in st.session_state:
        st.session_state.voice_attendance_results = None

    st.write(
        "Record audio of students saying 'I am present'. Then AI will recognize the students."
    )

    # -----------------------------
    # Get Students
    # -----------------------------
    enrolled_res = (
        supabase
        .table("subject_students")
        .select("*, students(*)")
        .eq("subject_id", selected_subject_id)
        .execute()
    )

    enrolled_students = enrolled_res.data

    if not enrolled_students:
        st.warning(
            "No students enrolled in this course"
        )
        return

    # -----------------------------
    # Audio Input
    # -----------------------------
    audio_data = st.audio_input(
        "Record classroom audio"
    )

    if audio_data:
        st.success(
            "Audio recorded successfully"
        )

    # -----------------------------
    # Analyze Button
    # -----------------------------
    if st.button(
        "Analyze Audio",
        width="stretch",
        type="primary"
    ):

        if audio_data is None:

            st.warning(
                "Please record audio first."
            )

        else:

            try:

                with st.spinner(
                    "Processing Audio..."
                ):

                    candidates_dict = {
                        s["students"]["student_id"]:
                        s["students"]["voice_embedding"]

                        for s in enrolled_students

                        if s["students"].get(
                            "voice_embedding"
                        )
                    }

                    if not candidates_dict:

                        st.error(
                            "No enrolled students have voice profiles registered"
                        )
                        return

                    audio_bytes = audio_data.read()

                    if not audio_bytes:

                        st.error(
                            "Audio file is empty."
                        )
                        return

                    detected_scores = process_bulk_audio(
                        audio_bytes,
                        candidates_dict
                    )

                    results = []
                    attendance_to_log = []

                    current_timestamp = (
                        datetime.now().strftime(
                            "%Y-%m-%dT%H:%M:%S"
                        )
                    )

                    for node in enrolled_students:

                        student = node["students"]

                        score = detected_scores.get(
                            student["student_id"],
                            0.0
                        )

                        is_present = score > 0

                        results.append({
                            "Name": student["name"],
                            "ID": student["student_id"],
                            "Source":
                                round(score, 4)
                                if is_present
                                else "-",
                            "Status":
                                "✅ Present"
                                if is_present
                                else "❌ Absent"
                        })

                        attendance_to_log.append({
                            "student_id":
                                student["student_id"],
                            "subject_id":
                                selected_subject_id,
                            "timestamp":
                                current_timestamp,
                            "is_present":
                                bool(is_present)
                        })

                    st.session_state.voice_attendance_results = (
                        pd.DataFrame(results),
                        attendance_to_log
                    )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

    # -----------------------------
    # Default Table (Absent)
    # -----------------------------
    if st.session_state.voice_attendance_results is None:

        preview_data = []

        for node in enrolled_students:

            student = node["students"]

            preview_data.append({
                "Name": student["name"],
                "ID": student["student_id"],
                "Source": "-",
                "Status": "❌ Absent"
            })

        st.divider()

        st.write(
            "Please review attendance before confirming."
        )

        st.dataframe(
            pd.DataFrame(preview_data),
            hide_index=True,
            width="stretch"
        )

    # -----------------------------
    # Show Final Results
    # -----------------------------
    else:

        st.divider()

        df_results, logs = (
            st.session_state
            .voice_attendance_results
        )

        show_attendance_result(
            df_results,
            logs
        )