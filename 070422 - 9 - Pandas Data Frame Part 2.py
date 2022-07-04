import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])

np.random.seed(101)

print(df)

# Printing whole data frame where value is greater than 0
print(df[df > 0])

# Printing data frame particular column where value is greater than 0

print(df[df['W'] > 0])
print(df[df['Z'] < 0])


print(df[df['Z'] < 0]['X'])
print(df[df['Z'] < 0][['X','Y']])


# Using different Operators Multiple conditional Selection
print(df[(df['W'] >0) & (df['X'] >1)])
print(df[(df['W'] >0) | (df['X'] >1)])

print(df.reset_index())
print(df)

# Setting new column on behalf of State Names

new_wind = "CA NY WY OR CO".split()
print(new_wind)

df["State"] = new_wind
print(df)
print(df.set_index('State'))