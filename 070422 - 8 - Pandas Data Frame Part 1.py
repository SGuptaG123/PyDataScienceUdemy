import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])

np.random.seed(101)

print(df)

# Selecting Columns from Data Frame
print(df['W'])
print(df[['W','Y']])

# Selecting Rows from Data Frame
print()
print(df.loc['A'])
print(df.iloc[3])

# Selecting a particular cell
print(df.loc['C','X'])
print(df.loc[['A','C'],['X','Y']])

# Adding a new column to the data frame

df['New'] = df['W'] + df['Z']
print(df)

# Dropping a column from the data frame

df.drop('New', axis=1, inplace=True)
print(df)

# Dropping a row from the data frame

df.drop('E', axis=0, inplace=True)
print(df)

print()
print(type(df['W']))
print(type(df))

print(df.shape)