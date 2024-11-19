import streamlit as st
import joblib

# Load the trained model
model = joblib.load("house_price_predic.pkl")

# Streamlit app layout
st.title("🏡 House Price Prediction App")
st.write("Estimate house prices based on key features.")

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=1)
square_footage = st.number_input("Square Footage", min_value=800, max_value=5000, value=800)
house_age = st.number_input("Age of the House (years)", min_value=1, max_value=100, value=1)

# Prediction button
if st.button("Predict House Price"):
    # Make prediction
    try:
        predicted_price = model.predict([[bedrooms, bathrooms, square_footage, house_age]])[0]
        st.success(f"The predicted house price is: ${predicted_price:,.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
