# Models

This directory contains the trained machine learning models used for the Home Credit Default Risk prediction project. Each `.pkl` file represents a serialized (pickled) version of a trained model, ready for loading and making predictions.

## Contents

* **`CatBoost.pkl`**:
    * **Model Type:** CatBoost Classifier
    * **Description:** A gradient boosting on decision trees library, often performing well with heterogeneous data and handling categorical features automatically. This file contains the trained CatBoost model.

* **`Logistic Regression.pkl`**:
    * **Model Type:** Logistic Regression
    * **Description:** A fundamental linear model for binary classification. This file contains the trained Logistic Regression model, providing a baseline for performance comparison.

* **`Random Forest.pkl`**:
    * **Model Type:** Random Forest Classifier
    * **Description:** An ensemble learning method that constructs a multitude of decision trees during training and outputs the mode of the classes (classification). This file contains the trained Random Forest model.

* **`XGBoost.pkl`**:
    * **Model Type:** XGBoost Classifier
    * **Description:** An optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable. This file contains the trained XGBoost model, known for its strong predictive performance in many Kaggle competitions.

## Usage

These models can be loaded using Python's `pickle` library (or `joblib` for better performance with large NumPy arrays) to make predictions on new data.

Example of loading a model:

```python
import pickle

# To load CatBoost model
with open('CatBoost.pkl', 'rb') as f:
    catboost_model = pickle.load(f)

# You can then use catboost_model.predict() or catboost_model.predict_proba()
