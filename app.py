import streamlit as st

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(layout="wide")

from sidebar import render_sidebar
render_sidebar()

# -----------------------
# GLOBAL CSS
# -----------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

/* Stat */
.stat {
    font-size: 28px;
    font-weight: bold;
}

/* Section spacing */
.section {
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# SESSION STATE
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------
# HEADER
# -----------------------
st.title("🫀 CardioGluco Risk Predictor")
st.markdown("**ML-powered early detection for heart disease and diabetes**")

# -----------------------
# STATS
# -----------------------
col1, col2, col3, col4 = st.columns(4)

total = len(st.session_state.history)
heart = len([h for h in st.session_state.history if h["type"] == "heart"])
diabetes = len([h for h in st.session_state.history if h["type"] == "diabetes"])
high_risk = len([h for h in st.session_state.history if h["risk"] == "High"])

def stat_card(col, value, label):
    with col:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat">{value}</div>', unsafe_allow_html=True)
            st.write(label)
            st.markdown('</div>', unsafe_allow_html=True)

stat_card(col1, total, "Total Predictions")
stat_card(col2, heart, "Heart Disease")
stat_card(col3, diabetes, "Diabetes")
stat_card(col4, high_risk, "High Risk Cases")

# -----------------------
# PREDICTOR SECTION
# -----------------------
st.markdown("## 🚀 Start Assessment")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ❤️ Heart Disease Predictor")
        st.write("""
        Uses classification models to assess cardiovascular risk based on 
        BP, cholesterol, and clinical data.
        """)
        if st.button("Start Heart Assessment"):
            st.switch_page("pages/1_Heart_Disease.py")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🩺 Diabetes Predictor")
        st.write("""
        Analyzes lifestyle, metabolic markers, and medical history.
        """)
        if st.button("Start Diabetes Assessment"):
            st.switch_page("pages/2_Diabetes.py")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# RECENT PREDICTIONS
# -----------------------
st.markdown("## 📜 Recent Predictions")

if len(st.session_state.history) == 0:
    st.info("No predictions yet")
else:
    for item in reversed(st.session_state.history[-5:]):
        with st.container():
            st.markdown('<div class="card section">', unsafe_allow_html=True)
            st.write(f"{item['type'].title()} → {item['risk']} Risk ({item['score']}%)")
            st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# ABOUT MODEL
# -----------------------
st.markdown("## 🤖 About the ML Models")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📊 Classification Approach")
    st.write("""
    Models use Logistic Regression and Random Forest concepts 
    for clinical risk scoring.
    """)

    st.markdown("### ⚙️ Feature Engineering")
    st.write("""
    BMI, risk factors, and clinical variables are derived 
    and weighted based on real-world significance.
    """)

    st.markdown('</div>', unsafe_allow_html=True)
