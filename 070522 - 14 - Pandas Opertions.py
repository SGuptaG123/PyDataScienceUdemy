import pandas as pd

df = pd.DataFrame({
    'A' : "foo foo foo bar bar bar".split(),
    'B' : "one one two two one one".split(),
    'C' : "x y x y x y".split(),
    'D' : [1,3,2,5,4,1]
})

print(df)
print()

x = df.pivot_table(values='D',index=['A','B'],columns=['C'])
print(x)


exit ()
import pandas as pd

df = pd.DataFrame({
    'col1' : [1,2,3,4],
    'col2' : [444,555,666,444],
    'col3' : ['abc', 'def', 'ghi', 'xyz']
}, index=['A','B','C','D'])


print(df)
print(df.head())

# Getting Unique value from column 2
print(df['col2'].unique())

# Counting unique values
print(len(df['col2'].unique()))
print(df['col2'].nunique())
print(df['col2'].value_counts())

# Selecting data
x = df[df['col1']>2]
print(x)

x = df[(df['col1']>2) & (df['col2']==444)]
print(x)


# Appyling the formula in the column using Apply Method

def multiple(num):
    return num*2

y = df['col1'].apply(multiple)
print(y)

z = df['col3'].apply(len)
print(z)

# Applying with lambda expression

y = df['col2'].apply(lambda x: x*2)
print(y)


# Removing the column permanently

df.drop('col3',axis=1,inplace=False)
print(df)


# Listing columns

print(df.columns)
print(df.index)

# Sorting the table by column names
print(df.sort_values('col2'))

# checking null values
print(df.isnull())



