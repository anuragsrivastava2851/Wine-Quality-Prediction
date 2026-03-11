import streamlit as st
import numpy as np
import joblib

model = joblib.load("wine_quality_model.pkl")

st.set_page_config(page_title="Wine Quality Predictor", layout="centered")

st.title("🍷 Wine Quality Prediction App")
st.write("Enter the chemical properties of wine to predict its quality.")

fixed_acidity = st.number_input(
    "Fixed Acidity (g/L)", value=7.4,
    help="Amount of fixed acids in grams per liter"
)

volatile_acidity = st.number_input(
    "Volatile Acidity (g/L)", value=0.70
)

citric_acid = st.number_input(
    "Citric Acid (g/L)", value=0.00
)

residual_sugar = st.number_input(
    "Residual Sugar (g/L)", value=1.9
)

chlorides = st.number_input(
    "Chlorides (g/L)", value=0.076
)

free_sulfur_dioxide = st.number_input(
    "Free Sulfur Dioxide (mg/L)", value=11
)

total_sulfur_dioxide = st.number_input(
    "Total Sulfur Dioxide (mg/L)", value=34
)

density = st.number_input(
    "Density (g/cm³)", value=0.9978
)

pH = st.number_input(
    "pH Level", value=3.51
)

sulphates = st.number_input(
    "Sulphates (g/L)", value=0.56
)

alcohol = st.number_input(
    "Alcohol (% by volume)", value=9.4
)

wine_type = st.selectbox("Wine Type", ["Red", "White"])

wine_type = 0 if wine_type == "Red" else 1

if st.button("Predict Quality 🍷"):
    
    sample = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                        residual_sugar, chlorides, free_sulfur_dioxide,
                        total_sulfur_dioxide, density, pH,
                        sulphates, alcohol, wine_type]])
    
    prediction = model.predict(sample)

    st.success(f"Predicted Wine Quality: {prediction[0]}")