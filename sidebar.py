import streamlit as st

def render_sidebar():

    st.sidebar.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        padding-top: 1rem;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .sidebar-subtitle {
        font-size: 13px;
        color: gray;
        margin-bottom: 20px;
    }

    .spacer {
        margin-top: 20px;
    }

    .disclaimer {
        padding: 12px;
        border-radius: 10px;
        background-color: #fff3cd;
        font-size: 12px;
        color: #856404;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.sidebar.markdown('<div class="sidebar-title">🧠 CardioGluco</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-subtitle">ML Risk Assessment</div>', unsafe_allow_html=True)

    # Navigation
    if st.sidebar.button("🏠 App Dashboard"):
        st.switch_page("app.py")

    if st.sidebar.button("❤️ Heart Disease"):
        st.switch_page("pages/1_Heart_Disease.py")

    if st.sidebar.button("🩺 Diabetes"):
        st.switch_page("pages/2_Diabetes.py")

    if st.sidebar.button("📘 Learn"):
        st.switch_page("pages/3_Learn.py")

    # Spacer
    st.sidebar.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # Disclaimer
    st.sidebar.markdown("""
    <div class="disclaimer">
    ⚠️ <b>Disclaimer:</b><br>
    This tool is for educational purposes only. 
    Always consult healthcare professionals for medical decisions.
    </div>
    """, unsafe_allow_html=True)
