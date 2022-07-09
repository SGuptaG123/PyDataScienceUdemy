''''
    website to decide adding a legend;

    https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
'''


# Figure Size and DPI


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# fig = plt.figure(figsize=(3,3), dpi=100)
# axes = fig.add_axes([0,0,1,1])
# axes.plot(x,y)


# # fig,axes = plt.subplots(figsize=(8,2), dpi=100)
# # axes.plot(x,y)


# fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2), dpi=100)
# axes[0].plot(x,y)
# axes[1].plot(y,x)

# Saving the images in .png, .jpg or other formats...

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
# axes.plot(x,y)
# axes.plot(y,x)

# Talking about legends


axes.plot(x,x**2, label='X squared')
axes.plot(x,x**3, label='X cubed')
axes.legend(loc=0)
# axes.legend(loc=10)
# axes.legend(loc=(0.1,0.1))


axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('My Title')




fig.savefig('MyPlot.png')
plt.tight_layout()
plt.show()




exit()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Sub Plotting in ShotrCut Way

fig,axes = plt.subplots(nrows=1, ncols=2)

# Method that we can use
# axes.plot(x,y)

# for axe_plot in axes:
#     axe_plot.plot(x,y)


# Plotting by index number

axes[0].plot(x,y)
axes[0].set_title("First Plot")

axes[1].plot(y,x)
axes[1].set_title("Second Plot")

plt.tight_layout()
plt.show()