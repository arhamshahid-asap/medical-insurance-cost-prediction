import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("🏥 Medical Insurance Cost Predictor")

st.write(
    "Enter the information below to estimate "
    "the medical insurance cost."
)

st.divider()


# ==========================================
# INPUT FIELDS
# ==========================================

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoking Status",
    ["no", "yes"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button("🔮 Predict Insurance Cost"):

    # --------------------------------------
    # Load dataset
    # --------------------------------------

    df = pd.read_csv("insurance.csv")

    # --------------------------------------
    # Encode categorical variables
    # --------------------------------------

    df_ml = pd.get_dummies(
        df,
        columns=["sex", "smoker", "region"],
        drop_first=True,
        dtype=int
    )

    # --------------------------------------
    # Features and target
    # --------------------------------------

    X = df_ml.drop("charges", axis=1)
    y = df_ml["charges"]

    # --------------------------------------
    # Train-test split
    # --------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # --------------------------------------
    # Scaling
    # --------------------------------------

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    # --------------------------------------
    # Train Linear Regression
    # --------------------------------------

    model = LinearRegression()

    model.fit(X_train_scaled, y_train)

    # --------------------------------------
    # Prepare user input
    # --------------------------------------

    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [1 if gender == "male" else 0],
        "smoker_yes": [1 if smoker == "yes" else 0],
        "region_northwest": [1 if region == "northwest" else 0],
        "region_southeast": [1 if region == "southeast" else 0],
        "region_southwest": [1 if region == "southwest" else 0]
    })

    # Ensure same feature order as training
    input_data = input_data[X.columns]

    # --------------------------------------
    # Scale input
    # --------------------------------------

    input_scaled = scaler.transform(input_data)

    # --------------------------------------
    # Make prediction
    # --------------------------------------

    prediction = model.predict(input_scaled)

    # --------------------------------------
    # Display result
    # --------------------------------------

    st.success(
        f"💰 Estimated Insurance Cost: ${prediction[0]:,.2f}"
    )