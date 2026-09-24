import streamlit as st


def subject_card(
    name,
    code,
    section,
    stats=None,
    footer_callback=None
):

    html_content = f"""<div style="background:white; padding:25px; border-radius:20px; border:1px solid #cbd5e1; margin-bottom:15px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
<h3 style="margin:0; color:#1e293b; font-size:28px; font-weight:700; text-align:left;">{name}</h3>
<p style="color:#64748b; font-size:16px; margin-top:12px; margin-bottom:0;">
Code: <span style="background:#E0E3FF; color:#5865F2; padding:4px 10px; border-radius:6px; font-weight:bold;">{code}</span>
&nbsp;&nbsp;|&nbsp;&nbsp;
Section: <b style="color:#1e293b;">{section}</b>
</p>
</div>"""

    st.markdown(html_content, unsafe_allow_html=True)

    if stats:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="👨‍🎓 Students",
                value=stats[0][2]
            )

        with col2:
            st.metric(
                label="📚 Classes",
                value=stats[1][2]
            )

    if footer_callback:
        footer_callback()