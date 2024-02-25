# -*- coding: utf-8 -*-
"""STOCK POLYNOMIAL REG

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s9oHen145OyU41Ou3zjnO_B_JAi40By-
"""

!pip install yfinance
import yfinance as yf
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

tsla = yf.Ticker("QCOM")
tsla_stock = tsla.history(period='max').reset_index()

plt.figure(figsize=(30,6))
plt.plot([i for i in range(7535)], tsla_stock.iloc[:,4])
plt.show()

import numpy as np

poly_feats = PolynomialFeatures(degree=10, include_bias=False)
X = np.array([i for i in range(7535)]).reshape(-1,1)
y = tsla_stock.iloc[:,4]

x_poly = poly_feats.fit_transform(X)

lin_reg = LinearRegression()
lin_reg.fit(x_poly, y)
y_predicted = lin_reg.predict(x_poly)
lin_reg.score(x_poly, y)

tsla_stock.head()

plt.figure(figsize=(20,6))
plt.plot([i for i in range(7535)], tsla_stock.iloc[:,4])
plt.plot(X, y_predicted, color='black')
plt.show()

temp = np.array([i for i in range(7000, 7900)]).reshape(-1,1)
trial = poly_feats.fit_transform(temp)
new = lin_reg.predict(trial)
plt.figure(figsize=(20,6))
plt.plot([i for i in range(7535)], tsla_stock.iloc[:,4])
plt.plot(X, y_predicted, color='black')
plt.plot(temp, new, color='red')
plt.show()

