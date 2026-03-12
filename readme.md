# 🍷 Wine Quality Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting the **quality of wine** based on its physicochemical properties using **Machine Learning techniques**. Wine quality is influenced by several measurable chemical attributes such as acidity, alcohol concentration, sulphates, and density. By training machine learning models on historical wine data, the system can estimate the **quality score of a wine sample**.

The project also includes a **web application built using Streamlit**, enabling users to interact with the model and obtain predictions by entering wine characteristics through a simple user interface.

This project demonstrates the **complete machine learning workflow**, from data preprocessing and model training to deployment of a predictive model.

---

## 🎯 Project Objectives

The main goals of this project are:

* Develop a **regression-based machine learning model** to predict wine quality.
* Explore and compare multiple machine learning algorithms.
* Improve prediction performance using **ensemble learning techniques**.
* Build an **interactive web application** for real-time predictions.
* Provide insights into which chemical properties most influence wine quality.

---

## 🧠 Machine Learning Models Used

The following regression models were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

To improve prediction performance, the final system uses an **ensemble model**:

**Voting Regressor**

This model combines predictions from multiple algorithms and averages them to produce a more stable and accurate prediction.

---

## 📊 Dataset Information

The dataset contains chemical measurements of **red and white wine samples**.
Each record represents a wine sample with multiple chemical attributes.

### Input Features

| Feature              | Description                                |
| -------------------- | ------------------------------------------ |
| Fixed Acidity        | Non-volatile acids present in wine         |
| Volatile Acidity     | Amount of acetic acid in wine              |
| Citric Acid          | Provides freshness and flavor              |
| Residual Sugar       | Sugar remaining after fermentation         |
| Chlorides            | Amount of salt present in wine             |
| Free Sulfur Dioxide  | Prevents microbial growth                  |
| Total Sulfur Dioxide | Total amount of SO₂ in wine                |
| Density              | Density of the wine                        |
| pH                   | Acidity level                              |
| Sulphates            | Wine additive contributing to preservation |
| Alcohol              | Alcohol percentage in wine                 |
| Wine Type            | Red or White wine                          |

### Target Variable

**Wine Quality Score**

The target value represents the **quality rating assigned to a wine sample**.

---

## ⚙️ Technologies & Tools

This project uses the following technologies:

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib

These tools were used for **data processing, model training, evaluation, and deployment**.

---

## 🔄 Machine Learning Workflow

The following steps were followed to build the predictive system:

1. Data Collection
2. Data Preprocessing and Cleaning
3. Feature Engineering
4. Exploratory Data Analysis (EDA)
5. Train–Test Data Splitting
6. Feature Scaling
7. Model Training
8. Model Evaluation and Comparison
9. Ensemble Learning using Voting Regressor
10. Feature Importance Analysis
11. Deployment with Streamlit Web Application

---

## 📈 Model Evaluation Metrics

To measure the performance of the regression models, the following metrics were used:

* **Mean Absolute Error (MAE)** – Average prediction error
* **Mean Squared Error (MSE)** – Squared difference between predictions and actual values
* **Root Mean Squared Error (RMSE)** – Standard deviation of prediction errors
* **R² Score** – Measures how well the model explains the variance in data

These metrics help evaluate **accuracy and reliability of predictions**.

---

## 💻 Interactive Web Application

A user-friendly **Streamlit web interface** has been developed to allow users to interact with the model.

### Application Features

* Simple and intuitive user interface
* Input fields for wine chemical properties
* Real-time prediction of wine quality
* Support for both **Red and White wine samples**

Users can enter the chemical attributes of wine and instantly receive a predicted **quality score**.

---

## 📂 Project Structure

```
wine-quality-prediction
│
├── app.py                  # Streamlit application
├── wine_quality_model.pkl  # Trained machine learning model
├── scaler.pkl              # Feature scaling object
├── notebook.ipynb          # Model development notebook
└── README.md               # Project documentation
```

---

## ▶️ How to Run the Project

Follow these steps to run the project locally.

### 1. Clone the Repository

```
git clone https://github.com/yourusername/wine-quality-prediction.git
```

### 2. Navigate to the Project Folder

```
cd wine-quality-prediction
```

### 3. Install Required Dependencies

```
pip install -r requirements.txt
```

### 4. Launch the Streamlit Application

```
streamlit run app.py
```

After running the command, the application will open in your browser:

```
http://localhost:8501
```

---

## 📊 Key Insights

During analysis, several features showed stronger influence on wine quality, including:

* Alcohol content
* Sulphates
* Volatile acidity

Feature importance analysis helped identify **which attributes contribute most to the prediction**.

---

## 🚀 Future Improvements

Potential improvements for the project include:

* Deploying the application on a cloud platform
* Adding advanced models such as Gradient Boosting or XGBoost
* Integrating visualization dashboards
* Adding automated feature selection
* Improving the UI with analytics and charts

---

## 👨‍💻 Author

**Anurag Srivastava**
B.Tech Computer Science – Data Science

Areas of Interest:

* Machine Learning
* Data Science
* Python Development

---

⭐ If you found this project useful, consider giving it a **star on GitHub**.
