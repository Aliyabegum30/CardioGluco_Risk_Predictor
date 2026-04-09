import streamlit as st
import numpy as np
import pandas as pd
import joblib

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(layout="wide")
from sidebar import render_sidebar
render_sidebar()
# -----------------------
# CARD CSS (ONLY WHEN USED)
# -----------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

/* Card style */
.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# LOAD MODEL
# -----------------------
model = joblib.load("diabetes/model/diabetes_model.pkl")
scaler = joblib.load("diabetes/model/diabetes_scaler.pkl")
feature_columns = joblib.load("diabetes/model/diabetes_features.pkl")

# -----------------------
# SESSION STATE
# -----------------------
if "predicted_diabetes" not in st.session_state:
    st.session_state.predicted_diabetes = False

if "prob" not in st.session_state:
    st.session_state.prob = None

# -----------------------
# TITLE (NO CARD)
# -----------------------
st.title("🩺 Diabetes Risk Assessment")
st.markdown("Classification model analyzing lifestyle, metabolic, genetic factors")

# -----------------------
# LAYOUT
# -----------------------
left, right = st.columns([1, 1.2])

# =======================
# LEFT → RESULT (NO CARD FOR TITLE)
# =======================
with left:

    st.markdown("## 📊 Result")

    # -------- RESULT CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if not st.session_state.predicted_diabetes:
        st.info("No Prediction Yet")

    else:
        prob = st.session_state.prob
        percentage = int(prob * 100)

        # GAUGE
        st.markdown(
            f"""
            <div style="display:flex;justify-content:center;">
                <div style="
                    width:220px;
                    height:220px;
                    border-radius:50%;
                    background: conic-gradient(#007bff {percentage}%, #ff9800 {percentage}%);
                    display:flex;
                    align-items:center;
                    justify-content:center;
                ">
                    <div style="
                        width:160px;
                        height:160px;
                        border-radius:50%;
                        background:white;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-size:30px;
                        font-weight:bold;
                    ">
                        {percentage}%
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if prob > 0.6:
            st.error("High Risk")
        elif prob > 0.3:
            st.warning("Moderate Risk")
        else:
            st.success("Low Risk")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- KEY FACTORS CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Key Risk Factors")

    if st.session_state.predicted_diabetes:
        factors = []

        if st.session_state.glucose >= 140:
            factors.append("High glucose")
        elif st.session_state.glucose >= 110:
            factors.append("Prediabetic glucose")

        if st.session_state.bmi >= 30:
            factors.append("Obesity")
        elif st.session_state.bmi >= 25:
            factors.append("Overweight")

        if st.session_state.bp >= 140:
            factors.append("High blood pressure")

        if st.session_state.family == "Yes":
            factors.append("Family history")

        if st.session_state.smoker == "Yes":
            factors.append("Smoking")

        if st.session_state.activity == "Low":
            factors.append("Low activity")

        if st.session_state.sleep == "Poor":
            factors.append("Poor sleep")

        if len(factors) == 0:
            st.success("No major risks")
        else:
            for f in factors:
                st.write(f"• {f}")
    else:
        st.info("Run prediction to view factors")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- RECOMMENDATIONS CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💡 Recommendations")

    if st.session_state.predicted_diabetes:
        recs = []

        if st.session_state.glucose >= 140:
            recs.append("Monitor glucose regularly")

        if st.session_state.bmi >= 30:
            recs.append("Reduce weight")

        if st.session_state.activity == "Low":
            recs.append("Increase activity")

        if st.session_state.smoker == "Yes":
            recs.append("Quit smoking")

        if st.session_state.bp >= 140:
            recs.append("Control BP")

        if st.session_state.sleep == "Poor":
            recs.append("Improve sleep")

        if len(recs) == 0:
            st.info("Maintain healthy lifestyle")
        else:
            for r in recs:
                st.write(f"• {r}")
    else:
        st.info("Run prediction to view recommendations")

    st.markdown('</div>', unsafe_allow_html=True)


# =======================
# RIGHT → INPUT
# =======================
with right:

    st.markdown("## 🧾 Input")

    # -------- PATIENT INFO CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 👤 Patient Info")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 10, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", 100, 220, 170)
    weight = st.number_input("Weight (kg)", 30, 150, 70)

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- CLINICAL CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧪 Clinical Data")

    glucose = st.number_input("Glucose", 70, 200, 100)
    bp = st.number_input("Blood Pressure", 80, 200, 120)

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- LIFESTYLE CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🏃 Lifestyle")

    activity = st.selectbox("Activity", ["Low", "Moderate", "High"])
    sleep = st.selectbox("Sleep", ["Poor", "Average", "Good"])
    smoker = st.selectbox("Smoker", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- FAMILY CARD --------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧬 Family History")

    family = st.selectbox("Family History", ["No", "Yes"])

    st.markdown('</div>', unsafe_allow_html=True)

    # -------- BUTTON --------
    if st.button("🚀 Run Prediction"):

        bmi = weight / ((height / 100) ** 2)
        skin_thickness = bmi * 0.5
        insulin = glucose * 0.8
        pregnancies = 0 if gender == "Male" else 2
        dpf = 0.7 if family == "Yes" else 0.2

        input_df = pd.DataFrame(
            np.zeros((1, len(feature_columns))),
            columns=feature_columns
        )

        input_df["Pregnancies"] = pregnancies
        input_df["Glucose"] = glucose
        input_df["BloodPressure"] = bp
        input_df["SkinThickness"] = skin_thickness
        input_df["Insulin"] = insulin
        input_df["BMI"] = bmi
        input_df["DiabetesPedigreeFunction"] = dpf
        input_df["Age"] = age

        input_scaled = scaler.transform(input_df)
        prob = model.predict_proba(input_scaled)[0][1]

        st.session_state.predicted_diabetes = True
        st.session_state.prob = prob
        st.session_state.glucose = glucose
        st.session_state.bmi = bmi
        st.session_state.family = family
        st.session_state.bp = bp
        st.session_state.activity = activity
        st.session_state.sleep = sleep
        st.session_state.smoker = smoker
        
        # ✅ HISTORY ADDED
        st.session_state.history.append({
            "type": "diabetes",
            "risk": "High" if prob > 0.6 else "Low",
            "score": int(prob * 100)
        })

        st.rerun()
