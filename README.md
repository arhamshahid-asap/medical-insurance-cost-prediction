# 🏥 Medical Insurance Cost Prediction

A Machine Learning project that predicts an individual's medical insurance cost based on demographic, lifestyle, and health-related factors.

The project uses Multiple Linear Regression to estimate insurance charges from features such as age, BMI, smoking status, gender, number of children, and region.

---

## 📌 Project Overview

Medical insurance costs can vary significantly depending on factors such as age, BMI, smoking status, family size, gender, and geographic region.

The objective of this project is to develop a Machine Learning regression model that can predict an individual's estimated medical insurance cost based on these factors.

The complete project follows the Machine Learning workflow:

Problem Definition → Data Collection → Data Exploration → 
Data Preprocessing → EDA → Model Training → Model Evaluation → 
Prediction → Deployment

---

## 🎯 Objectives

- Understand a real-world regression problem
- Explore and analyze the insurance dataset
- Clean and preprocess the data
- Convert categorical variables into numerical values
- Perform Exploratory Data Analysis
- Train a Multiple Linear Regression model
- Evaluate the model using regression metrics
- Build a prediction application
- Deploy the application using Streamlit

---

## 📊 Dataset

The project uses the Medical Cost Personal Dataset.

### Dataset Features

| Feature | Description |
|---|---|
| age | Age of the individual |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of children/dependents |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance cost |

### Target Variable

`charges`

The target variable represents the individual medical insurance cost.

### Problem Type

**Regression**

The model predicts a continuous numerical value.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas
2. Checked dataset shape and column names
3. Checked for missing values
4. Checked for duplicate records
5. Checked data types
6. Identified categorical variables
7. Applied One-Hot Encoding
8. Prepared the final dataset for Machine Learning

Categorical variables such as:

- Gender
- Smoking status
- Region

were converted into numerical values using One-Hot Encoding.

---

## 📈 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand relationships between the features and insurance charges.

The analysis included:

- Correlation analysis
- Age vs insurance charges
- BMI vs insurance charges
- Smoking status vs insurance charges
- Number of children vs insurance charges

### Important Observations

- Insurance charges generally increase with age.
- BMI has a relationship with insurance charges.
- Smoking status shows a strong difference in insurance charges.
- Age, BMI, and smoking status are important variables when predicting charges.
- The number of children has a comparatively weaker relationship with charges.

---

## 🤖 Machine Learning Model

### Multiple Linear Regression

The selected model is Multiple Linear Regression because the target variable `charges` is continuous.

The model learns the relationship between multiple input features and the insurance charges.

General equation:

ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ

Where:

- ŷ = predicted insurance cost
- b₀ = intercept
- b₁...bₙ = model coefficients
- x₁...xₙ = input features

The model was implemented using:

`sklearn.linear_model.LinearRegression`

---

## 🔀 Train-Test Split

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

The training data was used to train the model, while the testing data was used to evaluate its performance on unseen data.

---

## 📏 Model Evaluation

The trained model was evaluated using:

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted insurance charges.

### MSE

Mean Squared Error measures the average squared prediction error and gives more importance to larger errors.

### RMSE

Root Mean Squared Error is the square root of MSE and represents prediction error in the same unit as the target variable.

### R² Score

R² Score measures how much of the variation in insurance charges is explained by the model.

### Results

| Metric | Result |
|---|---:|
| MAE | ADD YOUR VALUE |
| MSE | ADD YOUR VALUE |
| RMSE | ADD YOUR VALUE |
| R² Score | ADD YOUR VALUE |

> Replace the values above with the actual values obtained from Phase 6.

---

## 🔮 Prediction Application

A Streamlit application was developed to allow users to enter:

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region

The application processes the input and uses the trained Linear Regression model to estimate the medical insurance cost.

### Example

Input:

Age: 35  
Gender: Male  
BMI: 28.5  
Children: 2  
Smoker: No  
Region: Southeast

Output:

Estimated Medical Insurance Cost: `$XXXX.XX`


## 📂 Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── app.py
├── insurance.csv
├── requirements.txt
├── README.md
├── Medical_Insurance_Cost_Prediction.ipynb