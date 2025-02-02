# Healthcare Cost Prediction

This project is a Streamlit application that predicts healthcare costs based on user inputs such as age, BMI, number of children, smoking status, and region.

## Project Structure
The project is organized into the following folders and files:

healthcare-cost-prediction/
├── data/ # Folder for raw and processed datasets
│ └── insurance.csv # Raw dataset used for training the model
├── notebooks/ # Jupyter notebooks for EDA and model training
│ ├── eda.ipynb # Exploratory Data Analysis (EDA) notebook
│ └── model_training.ipynb # Notebook for training the machine learning model
├── src/ # Python scripts for preprocessing and model training
│ └── model_training.py # Script to train and save the model
├── app.py # Streamlit app script for making predictions
├── model.pkl # Trained machine learning model
├── feature_names.txt # Feature names used during model training
├── requirements.txt # List of Python dependencies
└── README.md # Project description and instructions


## Dataset
The dataset is sourced from [Kaggle](https://www.kaggle.com/mirichoi0218/insurance). It includes the following features:
- `age`: Age of the individual.
- `sex`: Gender (male/female).
- `bmi`: Body Mass Index.
- `children`: Number of children.
- `smoker`: Smoking status (yes/no).
- `region`: Geographic region (northeast, northwest, southeast, southwest).
- `charges`: Healthcare costs (target variable).

## Exploratory Data Analysis (EDA)
EDA was performed using the `eda.ipynb` notebook. Key steps include:
- Visualizing distributions of features like `age`, `bmi`, and `charges`.
- Analyzing relationships between features using scatter plots and boxplots.
- Calculating correlations between features and the target variable (`charges`).

## Model Training
A Random Forest Regressor was trained to predict healthcare costs. The model was trained using the `model_training.ipynb` notebook or `src/model_training.py` script. The trained model (`model.pkl`) and feature names (`feature_names.txt`) are saved in the root directory.

## Web App
The Streamlit app (`app.py`) allows users to input their details and get an estimated healthcare cost. To run the app locally:
```bash
streamlit run app.py
```

## Features of the app

Input fields for `Age`, `BMI`, `Number of Children`, `Smoker`, and `Region` .
Predicts healthcare costs using the trained Random Forest model.
Handles one-hot encoding of categorical variables to match the training data structure.

## Deployment
The app can be deployed on platforms like:

Streamlit Cloud : Beginner-friendly and free for small projects.
Heroku: A cloud platform for deploying web applications.

## Requirements
Install the required libraries by running:

```bash
pip install -r requirements.txt

