import numpy as np
import pandas as pd

d = {
    'Company' : ['Goog', 'Goog', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person' : ['Sam', 'Charlie', 'Amy', 'Venessa', 'Carl', 'Sarah'],
    'Sales' : [200, 120, 340, 124,243, 350]
}

df = pd.DataFrame(d)
print(df)

# Group by method

gb = df.groupby('Company')
print(gb.mean())
print(gb.sum())
print(gb.std())


# Finding company sales by loc

print(gb.sum().loc['FB'])

x = df.groupby('Company').sum().loc['Goog']
print(x)

# Finding Min max and person name
highest_Sale = df.groupby('Company').max()
print(highest_Sale)

x_name = df.groupby('Company').max().loc['Goog'][0]
print('the person who does the highest sale for Google : ' + x_name)

x_name = df.groupby('Company').max().loc['FB'][0]
print('the person who does the highest sale for Google : ' + x_name)

desc = df.groupby('Company').describe()
print(desc)

desc_trans = df.groupby('Company').describe().transpose()
print(desc_trans)

desc_trans = df.groupby('Company').describe().transpose()['FB']
print(desc_trans)