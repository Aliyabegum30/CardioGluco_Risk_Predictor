import streamlit as st

st.set_page_config(layout="wide")
from sidebar import render_sidebar
render_sidebar()
# -----------------------
# SESSION STATE (for navigation)
# -----------------------
if "learn_section" not in st.session_state:
    st.session_state.learn_section = None

# -----------------------
# CSS
# -----------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

/* Card */
.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* Clickable cards */
.click-card {
    cursor: pointer;
    transition: 0.2s;
}
.click-card:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# TITLE
# -----------------------
st.title("📘 Learn")
st.markdown("Understand why each feature matters — clinically and in ML models")

# -----------------------
# TOP CARDS (SELECT SECTION)
# -----------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("❤️ Heart Disease"):
        st.session_state.learn_section = "heart"

with col2:
    if st.button("🩺 Diabetes Features"):
        st.session_state.learn_section = "diabetes"

with col3:
    if st.button("🤖 ML Methodology"):
        st.session_state.learn_section = "ml"

# =========================================================
# ❤️ HEART SECTION
# =========================================================
if st.session_state.learn_section == "heart":

    st.markdown("## ❤️ Heart Disease Features Explained")

    features = [
        ("Age",
         "Arterial stiffness increases with age. Risk rises sharply after 45/55.",
         "High coefficient in Logistic Regression. Strong monotonic increase."),

        ("Blood Pressure",
         "Hypertension damages arteries. Every +20mmHg doubles risk.",
         "High importance feature in Random Forest."),

        ("Cholesterol",
         "LDL forms plaques → blocks arteries.",
         "Non-linear effect. High values sharply increase risk."),

        ("Fasting Blood Sugar",
         "Damages blood vessels and increases inflammation.",
         "Binary threshold feature (>120 mg/dL)."),

        ("Heart Rate",
         "Indicates cardiovascular fitness.",
         "Moderate importance, interacts with age."),

        ("Smoking",
         "Damages endothelium and increases clotting.",
         "Strong binary predictor."),

        ("Chest Pain Type",
         "Typical angina strongly indicates disease.",
         "One-hot encoded categorical feature."),

        ("BMI",
         "Obesity increases cardiac workload.",
         "Derived feature, highly predictive.")
    ]

    for i, (name, why, ml) in enumerate(features, 1):

        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"### {i}. {name}")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**WHY IT MATTERS**")
                st.write(why)

            with c2:
                st.markdown("**ML ROLE**")
                st.write(ml)

            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 🩺 DIABETES SECTION
# =========================================================
elif st.session_state.learn_section == "diabetes":

    st.markdown("## 🩺 Diabetes Features Explained")

    features = [
        ("Fasting Glucose",
         "Measures blood sugar regulation. ≥126 = diabetes.",
         "Strongest predictor in most models."),

        ("HbA1c",
         "Average sugar over 3 months.",
         "Often best predictor but missing in basic datasets."),

        ("BMI",
         "Fat tissue causes insulin resistance.",
         "Top-3 feature. Non-linear behavior."),

        ("Physical Activity",
         "Improves glucose uptake.",
         "Ordinal feature, often ignored."),

        ("Family History",
         "Genetics influence insulin secretion.",
         "Often oversimplified in models."),

        ("Diet Quality",
         "Processed food increases risk.",
         "Rarely included but important."),

        ("Sleep",
         "Short sleep disrupts metabolism.",
         "U-shaped relationship."),

        ("Stress",
         "Raises cortisol → increases glucose.",
         "Moderate importance.")
    ]

    for i, (name, why, ml) in enumerate(features, 1):

        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"### {i}. {name}")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**WHY IT MATTERS**")
                st.write(why)

            with c2:
                st.markdown("**ML ROLE**")
                st.write(ml)

            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 🤖 ML SECTION
# =========================================================
elif st.session_state.learn_section == "ml":

    st.markdown("## 🤖 ML Methodology Deep Dive")

    topics = [
        ("Logistic Regression",
         "Models probability using sigmoid. Interpretable.",
         "Baseline model, linear boundary."),

        ("Random Forest",
         "Ensemble of trees capturing complex patterns.",
         "Handles non-linear relationships."),

        ("Feature Scaling",
         "Required for LR, not needed for RF.",
         "Common student mistake."),

        ("Class Imbalance",
         "Medical datasets often skewed.",
         "Use SMOTE or class weights."),

        ("Cross Validation",
         "Prevents unreliable evaluation.",
         "Use Stratified K-Fold."),

        ("Evaluation Metrics",
         "Accuracy is misleading.",
         "Use Recall, AUC, F1-score.")
    ]

    for i, (name, why, ml) in enumerate(topics, 1):

        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"### {i}. {name}")

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**WHY IT MATTERS**")
                st.write(why)

            with c2:
                st.markdown("**ML ROLE")
                st.write(ml)

            st.markdown('</div>', unsafe_allow_html=True)
