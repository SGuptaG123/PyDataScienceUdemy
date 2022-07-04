'''
    Multi Index or Index Hierarchy
'''

import numpy as np
import pandas as pd
from numpy.random import randn

outside = "G1 G1 G1 G2 G2 G2".split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(outside)
print(hier_index)


df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
print(df)


# How to fetch data from Multi Level Index Data Frame

x = df.loc['G1'].loc[1]
print(x)


print(df.index.names)

df.index.names = ['Groups', 'Num']
print(df)

y = df.loc['G2'].loc[2]['B']
print(y)

y = df.loc['G1'].loc[3]['A']
print(y)

z = df.xs(1,level='Num')
print(z)