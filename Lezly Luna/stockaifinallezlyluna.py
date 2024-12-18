# -*- coding: utf-8 -*-
"""StockAIFinalLezlyLuna.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hU_0uJ_3qLC7MnVkxmYrmYQMG4qwqp91
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from google.colab import files

#uploading the file
uploaded = files.upload()

#loading file
file_name = list(uploaded.keys())[0]
data = pd.read_csv(file_name)

#trying to show some rows of the data
print(data.head())

#preprocessing time
#setting 'Date' column to datetime format also setting as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

#checking for missing values
print("Missing values:")
print(data.isnull().sum())

#eliminate the ones with missing values
data = data.dropna()

#feature selection
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

#time to train using the train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model training
model = LinearRegression()
model.fit(X_train, y_train)

#model prediction
y_pred = model.predict(X_test)

#model evaluations
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')

#plots

#full size
plt.figure(figsize=(14, 7))

#making sure everything is in order
y_test_sorted = y_test.sort_index()
y_pred_sorted = pd.Series(y_pred, index=y_test.index).sort_index()

#plotting the main image
plt.plot(y_test_sorted.index, y_test_sorted, label='Actual Prices', color='blue')
plt.plot(y_pred_sorted.index, y_pred_sorted, label='Predicted Prices', color='red', linestyle='--', alpha=0.7)

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Actual vs Predicted Closing Prices')
plt.legend()
plt.show()

#creating some smaller ones to see beter
num_plots = 4  #how many i will do, seemed to be the best
window_size = len(y_test_sorted) // num_plots  #making sure its in sections

for i in range(num_plots):
    start = i * window_size
    end = start + window_size

    plt.figure(figsize=(14, 7))
    plt.plot(y_test_sorted.index[start:end], y_test_sorted[start:end], label='Actual Prices', color='blue')
    plt.plot(y_pred_sorted.index[start:end], y_pred_sorted[start:end], label='Predicted Prices', color='red', linestyle='--', alpha=0.7)

    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(f'Zoomed In Image {i + 1})')
    plt.legend()
    plt.show()