import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from termcolor import colored

#Extracting data
data = pd.read_csv('aapl.csv', encoding='latin-1')
X = data[data.columns[:-1]]
y = X.iloc[:,1:2].values
X = X.values[0:-1,1:-1]
m = X.shape[0]
X_train, y_train = [], []
for i in range(60,m+1):
    X_train.append(X[i-60:i,0])
    y_train.append(y[i,0])
X_train, y_train = np.array(X_train), np.array(y_train).reshape(-1,1)

print(X_train.shape,y_train.shape)
