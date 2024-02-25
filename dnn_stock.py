# -*- coding: utf-8 -*-
"""DNN Stock

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pScgV9MJ4lwhqjok9M-pjmywd-0FdtGM
"""

import requests
import pandas as pd

# def make_df(companies):
#   eps_final = pd.DataFrame()
#   for company in companies:
#     url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={company}&apikey=GNQSBVXWBU0KWL1I'
#     r = requests.get(url)
#     data = r.json()
#     eps = pd.DataFrame(data['quarterlyEarnings'])
#     eps = eps[['reportedDate', 'estimatedEPS']]
#     eps.rename(columns={'reportedDate':'Date', 'estimatedEPS':'EPS'}, inplace=True)
#     eps_final = pd.merge()

import requests
import pandas as pd
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=GNQSBVXWBU0KWL1I'
r = requests.get(url)
data = r.json()
eps = pd.DataFrame(data['quarterlyEarnings'])
eps = eps[['reportedDate', 'estimatedEPS']]
eps.rename(columns={'reportedDate':'Date', 'estimatedEPS':'EPS'}, inplace=True)
eps.head()

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

stock_price = pd.DataFrame(data['Monthly Time Series'])
low = stock_price.iloc[2,:]
low_val = low.values
low_ind = low.index

stock_price = pd.DataFrame()
stock_price['Date'] = low_ind
stock_price['Price'] = low_val

stock_price.head()

dates=[]
for i in stock_price['Date']:
  date = i[:7]
  dates.append(date)
stock_price['Date'] = dates
stock_price.head()

dates=[]
for i in eps['Date']:
  date = i[:7]
  dates.append(date)
eps['Date'] = dates
eps.head()

eps_rounded=[]
for i in eps['EPS']:
  i = float(i)
  new_eps = round(i,1)
  eps_rounded.append(new_eps)
eps['EPS'] = eps_rounded
eps.head()

df = pd.merge(stock_price, eps, how='inner', on='Date')
df.shape

df = df.iloc[:,1:]
df.head()

import matplotlib.pyplot as plt
plt.figure(figsize=(40,30))
plt.scatter(df['EPS'], df['Price'])
plt.show()

layer = layers.Dense(3, input_shape=(1,4))
print(layer.weights)
x = tf.ones((2, 5))
print(x)
y = layer(x)
print(y)
layer.weights