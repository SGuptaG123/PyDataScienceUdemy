from statistics import mean
import numpy as np
import pandas as pd

d = {
    'A':[1,2, np.nan],
    'B':[5, np.nan, np.nan],
    'C':[1,2,3]
}

df = pd.DataFrame(d)
print(df)

# df.dropna(axis=0, inplace=True)
# print(df)


# df.dropna(axis=1, inplace=True)
# print(df)

# Deleting the na values from Data Frame..
print(df.dropna(axis=0))
print(df.dropna(axis=1))
print(df.dropna(thresh=2))

# Filling the na values with another value in Data Frame..

print(df.fillna(value='My Value'))

# Filling the value of Column A with the Mean of the value.

print(df['A'].fillna(value=df['A'].mean()))