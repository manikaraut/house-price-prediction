# House Price Prediction Project using Linear Regression

## Overview
This project predicts house prices using a Linear Regression model based on features like area, number of bedrooms, and bathrooms. The goal is to estimate house prices using these attributes from the dataset.

## Project Structure

house_price_predction/
│
├── dataset/
│   └── Housing.csv
│
├── notebook/            
│   └── price_prediction.ipynb
│ 
|__ .gitignore
|
|__README.md
|
└── requirement.txt

## Dataset Description
- price: The target variable (house price).
- area: The area of the house in square feet.
- bedrooms: The number of bedrooms in the house.
- bathrooms: The number of bathrooms in the house.
- stories: The number of floors/stories in the house.
- mainroad: Whether the house is on the main road (yes/no).
- guestroom: Whether the house has a guestroom (yes/no).
- basement: Whether the house has a basement (yes/no).
- hotwaterheating: Whether the house has hot water heating (yes/no).
- airconditioning: Whether the house has air conditioning (yes/no).
- parking: The number of parking spaces available.
- prefarea: Whether the house is in a preferred area (yes/no).
- furnishingstatus: The furnishing status of the house (furnished/semifurnished/unfurnished).

## Steps
1. Exploratory Data Analysis (EDA): Visualize distributions, correlations, and relationships between features.
2. Train-Test Split: The dataset is split into training and testing sets.
3. Train the Model: Train a Linear Regression model to predict house prices.
4. Prediction: After training the model, predictions are made on the test data
5. Model Evaluation: Evaluate the model using Mean Squared Error (MSE) and R-squared metrics.

## Requirements
- Python 3.x
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - streamlit

## Installation
1. Clone the repository:
bash
git clone [repository-url]
cd house_price_prediction

2. Create Virtual Environment file
python env -m virtualenv env
env\Scripts\activate

3. Install required packages:
bash
pip install pandas scikit-learn matplotlib seaborn

## Results
- Mean Squared Error: [Value]
- R-squared: [Value]


