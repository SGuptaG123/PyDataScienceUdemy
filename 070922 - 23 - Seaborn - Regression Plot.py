import matplotlib.pyplot as plt
from numpy import block
import seaborn as sns

tips = sns.load_dataset('tips')

print(tips.head(5))

# sns.lmplot(x='total_bill', y='tip', data=tips)
# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'])
# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'], scatter_kws={'s' :100}) 
# sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
# sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')

# sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6, size=8)

plt.show(block=True)