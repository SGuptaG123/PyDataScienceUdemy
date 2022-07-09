'''Dataset available for seaborn library
    tips, fmri, diamonds, penguins

    Categorical Plot available
    bar plot, countplot, boxplot, violinplot, stripplot, swarmplot, factorplot
'''

from posixpath import split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head(5))
print(tips.info())

# Bar Plot
# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# Count Plot
# sns.countplot(x='sex', data=tips)

# Box Plot
# sns.boxplot(data=tips, x='day',y='total_bill')
# sns.boxplot(data=tips, x='day',y='total_bill', hue='smoker')

# Voilen Plot
# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker')
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# Strip plot
# sns.stripplot(x='day', y='total_bill', data=tips, hue='sex',jitter=True, split=True)

# Swarm plot
# sns.swarmplot(x='day', y='total_bill', data=tips)

# mixing swarm plot and violinplot
# sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
# sns.violinplot(x='day', y='total_bill', data=tips)

# factor plot
sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')

plt.show(block=True) 