''' two types of grid in Seaborn
    PairGrid,
    FacetGrid
'''


import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')

g = sns.FacetGrid(tips, row='time', col='smoker')
# g.map(sns.distplot, 'total_bill')

g.map(sns.scatterplot, 'total_bill', "tip")


plt.show(block=True)

exit()

import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

print(iris.head())
print(iris['species'].unique())

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)


plt.show(block=True)