# 🚗 Used Car Price Prediction

An end-to-end Machine Learning project that predicts the **resale price of used cars** based on their specifications, brand, manufacturing year, usage and location.

The project covers the complete ML workflow, from Exploratory Data Analysis (EDA) and data preprocessing to model training, evaluation and deployment using Streamlit.

🔗 **Live Demo:** [Used Car Price Prediction](https://used-car-price-prediction-abc.streamlit.app/)

📂 **GitHub Repository:** [Used-Car-Price-Prediction](https://github.com/arushparikh16-netizen/Used-Car-Price-Prediction)

---

## 📌 Project Overview

Buying or selling a second-hand car can be challenging because its resale value depends on several factors, including its age, brand, mileage, engine capacity, kilometers driven and ownership history.

This project uses regression-based Machine Learning algorithms to estimate the resale price of a used car based on user-provided information.

A Streamlit web application allows users to enter car details and receive an estimated resale price instantly.

## ✨ Features

- Predicts the estimated resale price of used cars.
- Supports multiple car brands and locations.
- Considers manufacturing year, kilometers driven, fuel type, transmission and ownership.
- Performs automated preprocessing through Scikit-learn pipelines.
- Uses logarithmic transformations to handle skewed numerical features and the target variable.
- Uses RidgeCV for cross-validated regularization parameter selection.
- Interactive web application built using Streamlit.
- Deployed online using Streamlit Community Cloud.

## 📊 Dataset

The dataset contains information about used car listings and their selling prices.

**Features used for prediction:**

| Feature | Description |
|---|---|
| Brand | Manufacturer of the car |
| Location | City where the car is listed |
| Year | Manufacturing year |
| Kilometers_Driven | Total distance driven |
| Fuel_Type | Petrol, Diesel, CNG, LPG or Electric |
| Transmission | Manual or Automatic |
| Owner_Type | Previous ownership category |
| Mileage | Fuel efficiency |
| Engine | Engine capacity in CC |
| Power | Engine power in bhp |
| Seats | Seating capacity |

**Target Variable:** `Price` — resale price of the used car, measured in lakhs.

## 🔍 Exploratory Data Analysis

EDA was performed using Pandas, Matplotlib, Seaborn and Pandas Profiling.

The analysis included:

- Understanding dataset structure, data types and statistical summaries.
- Identifying missing values and duplicate records.
- Studying numerical feature distributions.
- Detecting outliers using box plots and the IQR method.
- Analysing categorical feature distributions.
- Understanding relationships between car specifications and resale prices.
- Examining the distribution and skewness of the target variable.

## 🤖 Machine Learning Models

The following regression algorithms were implemented and evaluated:

1. Linear Regression
2. Lasso Regression
3. Ridge Regression

### Model Comparison

| Model | Test R² | Test MAE | Test RMSE |
|---|---:|---:|---:|
| Linear Regression | 0.886 | 1.543 | 9.571 |
| Lasso Regression (LassoCV) | 0.897 |  1.542 | 8.830 |
| Ridge Regression (RidgeCV) | 0.888 |  1.540 | 9.583 |

**Final Selected Model:** Lasso Regressio with LassoCV

## 🖥️ Web Application

The project is deployed using Streamlit Community Cloud.

Users can:
- Select a car brand and location.
- Enter manufacturing year and kilometers driven.
- Select fuel type, transmission and ownership.
- Enter mileage, engine capacity, power and seating capacity.
- Get an estimated used car resale price.

🔗 **Try the application:** https://used-car-price-prediction-abc.streamlit.app/

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| EDA | Pandas Profiling |
| Machine Learning | Scikit-learn |
| Model Selection | RidgeCV |
| Preprocessing | ColumnTransformer, Pipeline |
| Model Serialization | Joblib |
| Web Framework | Streamlit |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |

## 📁 Project Structure

```text
Used-Car-Price-Prediction/
│
├── app.py
├── car_price_model.pkl
├── brands.pkl
├── locations.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/arushparikh16-netizen/Used-Car-Price-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Used-Car-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🔮 Future Improvements

- Experiment with advanced ensemble models such as Random Forest and XGBoost.
- Improve prediction accuracy through additional feature engineering.
- Incorporate newer used-car listings for better market relevance.
- Add model explainability using SHAP.
- Improve input validation and handling of unseen categories.
- Provide more reliable price estimates across different car segments.

## 👨‍💻 Author

**Arush Parikh**

Computer Science and Engineering (AI & ML)

GitHub: [@arushparikh16-netizen](https://github.com/arushparikh16-netizen)

---

⭐ If you find this project interesting, feel free to explore the repository and try the live application.

**Built as part of my journey in Machine Learning and AI.**
