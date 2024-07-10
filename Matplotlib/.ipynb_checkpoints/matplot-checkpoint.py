import os
import csv
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt

print(np.__version__)
print(pd.__version__)

plt.style.use('fivethirtyeight')

# Correct file path
data = pd.read_csv(r'D:\Python\Matplotlib\data.csv')

# Alternatively, using double backslashes
# data = pd.read_csv('D:\\Python\\Matplotlib\\data.csv')