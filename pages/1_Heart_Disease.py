import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(layout="wide")
from sidebar import render_sidebar
render_sidebar()
# -----------------------
# CSS
# -----------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.result-card {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, #e6f4ea, #f0fdf4);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# LOAD FILES
# -----------------------
model = joblib.load("heart/model/model.pkl")
scaler = joblib.load("heart/model/scaler.pkl")
feature_columns = joblib.load("heart/model/feature_columns.pkl")

# -----------------------
# SESSION STATE
# -----------------------
if "predicted" not in st.session_state:
    st.session_state.predicted = False
if "prob" not in st.session_state:
    st.session_state.prob = None
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# -----------------------
# TITLE
# -----------------------
st.title("❤️ Heart Disease Risk Assessment")
st.caption("ML-based clinical risk evaluation system")

# -----------------------
# MAIN LAYOUT
# -----------------------
left, right = st.columns(2)

# =======================
# RESULT SIDE
# =======================
with left:

    st.markdown("## 📊 Result")

    if not st.session_state.predicted:
        st.info("No Prediction Yet")

    else:
        prob = st.session_state.prob
        prediction = st.session_state.prediction

        # ---------- RESULT CARD ----------
        st.markdown('<div class="result-card">', unsafe_allow_html=True)

        # center gauge
        c1, c2, c3 = st.columns([1, 2, 1])

        with c2:
            fig, ax = plt.subplots(figsize=(2, 2))

            ax.pie(
                [prob, 1 - prob],
                startangle=90,
                counterclock=False,
                wedgeprops={'width': 0.25}
            )

            ax.text(0, 0, f"{prob*100:.0f}%", ha='center', va='center', fontsize=12)

            plt.tight_layout()
            st.pyplot(fig, use_container_width=False)

        if prediction[0] == 1:
            st.error("⚠️ High Risk")
        else:
            st.success("✅ Low Risk")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- KEY FACTORS ----------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🔍 Key Risk Factors")

        if prob > 0.6:
            factors = [
                "High probability of cardiovascular disease",
                "Possible high cholesterol or BP",
                "Stress on heart indicators detected"
            ]
        elif prob > 0.3:
            factors = [
                "Moderate risk detected",
                "Lifestyle factors may contribute",
                "Monitor health indicators"
            ]
        else:
            factors = [
                "Stable heart condition",
                "No major risk indicators",
                "Healthy profile overall"
            ]

        for f in factors:
            st.write(f"- {f}")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- RECOMMENDATIONS ----------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💡 Recommendations")

        if prob > 0.6:
            st.write("- Consult a cardiologist immediately")
            st.write("- Reduce salt & fat intake")
            st.write("- Regular monitoring required")
        elif prob > 0.3:
            st.write("- Improve diet and reduce junk food")
            st.write("- Exercise regularly")
            st.write("- Routine health checkups")
        else:
            st.write("- Maintain current healthy lifestyle")
            st.write("- Stay active")
            st.write("- Annual checkup recommended")

        st.markdown('</div>', unsafe_allow_html=True)

# =======================
# INPUT SIDE
# =======================
with right:

    st.markdown("## 🧾 Input Details")

    # ---------- PATIENT INFO ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 👤 Patient Info")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Patient Name")
        age = st.number_input("Age", 20, 100, 50)

    with col2:
        sex = st.selectbox("Gender", ["Female", "Male"])
        weight = st.number_input("Weight (kg)", 30, 150, 70)

    height = st.number_input("Height (cm)", 100, 220, 170)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- CLINICAL DATA ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🏥 Clinical Data")

    trestbps = st.number_input("Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 400, 200)
    thalach = st.number_input("Heart Rate", 60, 220, 150)
    oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- LIFESTYLE ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧬 Lifestyle")

    fbs = st.selectbox("Fasting Blood Sugar > 120", ["No", "Yes"])
    exang = st.selectbox("Exercise Angina", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- BUTTON ----------
    if st.button("🚀 Run Prediction Model"):

        input_df = pd.DataFrame(
            np.zeros((1, len(feature_columns))),
            columns=feature_columns
        )

        input_df["age"] = age
        input_df["trestbps"] = trestbps
        input_df["chol"] = chol
        input_df["thalch"] = thalach
        input_df["oldpeak"] = oldpeak

        if "sex_Male" in input_df.columns:
            input_df["sex_Male"] = 1 if sex == "Male" else 0

        if "fbs_Yes" in input_df.columns:
            input_df["fbs_Yes"] = 1 if fbs == "Yes" else 0

        if "exang_Yes" in input_df.columns:
            input_df["exang_Yes"] = 1 if exang == "Yes" else 0

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)
        prob = model.predict_proba(input_scaled)[0][1]

        st.session_state.predicted = True
        st.session_state.prediction = prediction
        st.session_state.prob = prob
        
        # ✅ HISTORY ADDED
        st.session_state.history.append({
            "type": "heart",
            "risk": "High" if prob > 0.6 else "Low",
            "score": int(prob * 100)
        })

        st.rerun()
