import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the feature names used during training
with open('feature_names.txt', 'r') as f:
    feature_names = f.read().split(',')

# Create input fields
st.title("Healthcare Cost Prediction")
age = st.number_input("Age", min_value=18, max_value=100)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0)
children = st.number_input("Number of Children", min_value=0, max_value=10)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Preprocess inputs
smoker_yes = 1 if smoker == "Yes" else 0
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0

# Create a DataFrame with the same structure as X_train
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'smoker_yes': [smoker_yes],
    'region_northwest': [region_northwest],
    'region_southeast': [region_southeast],
    'region_southwest': [region_southwest]
})

# Ensure the input data has the same columns as the training data
input_data = input_data.reindex(columns=feature_names, fill_value=0)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Healthcare Cost: ${prediction[0]:.2f}")