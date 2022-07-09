import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flight = sns.load_dataset('flights')

# x = tips.corr()

# print(tips.head(5))
# print(x)

# sns.heatmap(x, annot=x, cmap='coolwarm')


# playing around pivot table in seaborn data set
# print(flight.head(5))


y = flight.pivot_table(index='month', columns='year', values='passengers')

# sns.heatmap(y, cmap='coolwarm')
# sns.heatmap(y, cmap='coolwarm', linewidths=1, linecolor='white')

# Cluster Map
sns.clustermap(y,cmap='coolwarm', linewidths=1, linecolor='white', standard_scale=1)

plt.show(block=True)