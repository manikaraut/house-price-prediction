import os
import joblib
import pandas as pd
import streamlit as st

# Load model and encoder with error handling
model_path = r"C:/Users/Lenovo/house-price-prediction/notebook/house_pred.pkl"
encoder_path = r"C:/Users/Lenovo/house-price-prediction/notebook/onehot_encoder.pkl"


# Load model and encoder
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

# Streamlit UI
st.title("🏡 House Price Prediction")
st.write("Enter house details below to predict the price:")

# Define user input fields
area = st.number_input("Area (sq ft):", min_value=500, step=50)
bedrooms = st.number_input("Bedrooms:", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms:", min_value=1, step=1)
stories = st.number_input("Stories:", min_value=1, step=1)
parking = st.number_input("Parking Spaces:", min_value=0, step=1)

# Categorical inputs
mainroad = st.selectbox("Main Road Access:", ["No", "Yes"])
guestroom = st.selectbox("Guestroom:", ["No", "Yes"])
basement = st.selectbox("Basement:", ["No", "Yes"])
hotwaterheating = st.selectbox("Hot Water Heating:", ["No", "Yes"])
airconditioning = st.selectbox("Air Conditioning:", ["No", "Yes"])
prefarea = st.selectbox("Preferred Area:", ["No", "Yes"])
furnishingstatus = st.selectbox("Furnishing Status:", ["Furnished", "Semi-Furnished", "Unfurnished"])

# Convert input to DataFrame
input_data = pd.DataFrame([{
    "area": area, "bedrooms": bedrooms, "bathrooms": bathrooms, "stories": stories, "parking": parking,
    "mainroad": "yes" if mainroad == "Yes" else "no",
    "guestroom": "yes" if guestroom == "Yes" else "no",
    "basement": "yes" if basement == "Yes" else "no",
    "hotwaterheating": "yes" if hotwaterheating == "Yes" else "no",
    "airconditioning": "yes" if airconditioning == "Yes" else "no",
    "prefarea": "yes" if prefarea == "Yes" else "no",
    "furnishingstatus": furnishingstatus.lower()
}])

# Encode categorical data
try:
    encoded_input = encoder.transform(input_data.select_dtypes(include=['object'])).toarray()
    encoded_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out())
except AttributeError:
    st.error("Encoder is not fitted properly. Retrain and save it.")
    st.stop()

# Merge with numerical data
final_input = pd.concat([input_data.select_dtypes(exclude=['object']), encoded_df], axis=1)

# Predict button
if st.button("🔍 Predict Price"):
    try:
        prediction = model.predict(final_input)
        st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
