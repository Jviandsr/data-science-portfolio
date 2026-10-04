---
layout: default
title: "Project 2: Housing Price Predictive Modeling"
---

# Project 2: Real Estate Market Predictive Modeling

## Overview
This project evaluates housing price dynamics using the King County House Sales dataset[cite: 1]. The objective is to compare linear and non-linear machine learning models to predict residential property sale prices.

## Research Question
To what extent can structural features (square footage, bedrooms, grade) and location predict residential sale prices, and which features contribute most significantly to pricing variance[cite: 1]?

## Methodology & Models
1. **Multiple Linear Regression:** Used to establish baseline linear coefficients and interpret individual feature impact[cite: 1].
2. **Random Forest Regressor:** Implemented to capture non-linear relationships and complex feature interactions[cite: 1].

## Code & Implementation
The core Python script for data preprocessing, model training, and evaluation:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load data and train models
df = pd.read_csv('kc_house_data.csv')
features = ['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'grade']
X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression().fit(X_train, y_train)
print(f"LR R^2: {r2_score(y_test, lr.predict(X_test)):.4f}")

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)
print(f"RF R^2: {r2_score(y_test, rf.predict(X_test)):.4f}")
