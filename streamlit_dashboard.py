import streamlit as st
import requests
import json

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="ML API Dashboard", layout="wide")

st.title("ML API Dashboard")
st.write("Manage users and machine learning models")


st.header("User Management")

with st.form("signup_form"):
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Create User")
    if submitted:
        res = requests.post(f"{API_URL}/signup", json={"username": username, "password": password})
        st.write(res.json())

with st.form("tokens_form"):
    st.subheader("Add Tokens")
    username_t = st.text_input("Username to add tokens")
    amount = st.number_input("Amount", min_value=1, step=1)
    cc = st.text_input("Credit Card")
    submitted_t = st.form_submit_button("Add Tokens")
    if submitted_t:
        res = requests.post(
            f"{API_URL}/add_tokens",
            json={"username": username_t, "credit_card": cc, "amount": amount}
        )
        st.write(res.json())


st.header("Model Management")

uploaded_file = st.file_uploader("Upload CSV file for training", type=["csv"])
features = st.text_input("Features (comma separated)")
label = st.text_input("Label column")

if st.button("Train Model"):
    if uploaded_file is not None:
        res = requests.post(
            f"{API_URL}/train",
            files={"file": uploaded_file},
            data={"features": features, "label": label}
        )
        st.write(res.json())
    else:
        st.warning("Please upload a CSV file")

if st.button("Show Models"):
    res = requests.get(f"{API_URL}/models")
    st.json(res.json())


st.header("Prediction")

model_name = st.text_input("Model name for prediction")
json_input = st.text_area("Enter JSON data for prediction (list of objects)")

if st.button("Predict"):
    try:
        data = json.loads(json_input)
        res = requests.post(
            f"{API_URL}/predict",
            json={"model_name": model_name, "data": data}
        )
        st.json(res.json())
    except Exception as e:
        st.error(f"Invalid input: {e}")