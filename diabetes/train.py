import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv("data/diabetes.csv")

# -----------------------
# CLEAN DATA (REPLACE 0s)
# -----------------------
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in cols:
    df[col] = df[col].replace(0, df[col].median())

# -----------------------
# FEATURES & TARGET
# -----------------------
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# -----------------------
# SPLIT
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# SCALE
# -----------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# MODEL
# -----------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------
# EVALUATE
# -----------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

# -----------------------
# SAVE MODEL
# -----------------------
joblib.dump(model, "model/diabetes_model.pkl")
joblib.dump(scaler, "model/diabetes_scaler.pkl")
joblib.dump(X.columns.tolist(), "model/diabetes_features.pkl")

print("Model, scaler, and features saved successfully!")
