'''
    Colormaps documentation page
    https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html

'''


import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='summer')
plt.show(block=True)

exit()


import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# plt.figure(figsize=(12,3))

sns.set_context('notebook')
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine()


plt.show(block=True)