import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("travel_time_model.pkl")

st.set_page_config(page_title="AI Travel Time Predictor", layout="centered")

st.title("🚗 AI Based Travel Time Detector")
st.write("Enter trip details to predict travel time")

# ---- INPUTS (example – adjust to your dataset columns) ----
distance = st.number_input("Distance (km)", min_value=0.0, step=0.1)
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
weather = st.selectbox("Weather", ["Clear", "Rainy", "Foggy"])
hour = st.number_input("Hour of Day (0–23)", min_value=0, max_value=23)

# ---- PREDICTION ----
if st.button("Predict Travel Time"):
    input_data = pd.DataFrame([{
        "Distance": distance,
        "Traffic": traffic,
        "Weather": weather,
        "Hour": hour
    }])

    prediction = model.predict(input_data)

    st.success(f"🕒 Estimated Travel Time: {prediction[0]:.2f} minutes")
