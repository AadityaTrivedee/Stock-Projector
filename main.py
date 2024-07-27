import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from termcolor import colored

#Extracting data
data = pd.read_csv('aapl.csv', encoding='latin-1')
X = data[data.columns[:-1]]
y = data[data.columns[-1]]
