# Imports
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = 'weekly_prices.csv'

df = pd.read_csv(data)
print(df)

model = LinearRegression()