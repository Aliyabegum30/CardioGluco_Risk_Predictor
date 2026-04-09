import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("data/heart_disease_uci.csv")

# Create target
df["target"] = df["num"].apply(lambda x: 1 if x > 0 else 0)

# Drop unnecessary columns
df = df.drop(["id", "dataset", "num"], axis=1)

# Handle missing values
df = df.dropna()

# Split
X = df.drop("target", axis=1)
y = df["target"]

# One-hot encoding
X = pd.get_dummies(X, drop_first=True)

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save everything
joblib.dump(model, "model/model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(X.columns, "model/feature_columns.pkl")

print("✅ Model saved successfully!")
