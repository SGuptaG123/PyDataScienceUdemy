'''
    seaborn Plots 
        .distplot, .jointplot, .pairplot, .rugplot
        barplot, countplot, boxplot, violinplot, stripplot, swarmplot, factorplot
'''

import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')
print(tips.head(5))

# Dist Plot
# sns.displot(tips['total_bill'], kde=False, bins=100)

# Joint Plot

# sns.jointplot(x='total_bill',y='tip',data=tips)
# sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')
# sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')
# sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')


# Pair Plot
# sns.pairplot(data=tips, hue='sex', palette='coolwarm')

# Rug plot
# sns.rugplot(tips['total_bill'])

# kde Plot
sns.kdeplot(tips['total_bill'])


plt.show(block=True)