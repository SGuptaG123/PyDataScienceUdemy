import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,c='green',lw= 3,marker='o')
axes.set_xlim([0,1])
axes.set_ylim([0,2])


plt.tight_layout()
plt.show()

exit()


'''
    Search on google for more hex code for RGB colors.

    color, linewithdth(lw), linestyle(ls)
    axes.plot(x,y, c='purple', lw = 3, ls=":")
    axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", ms = 10, mfc= 'g')

'''


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])


# For color of the plotted line==================================
# axes.plot(x,y, 'g')
# axes.plot(x,y, color='orange')
# axes.plot(x,y, color='purple')


# For width of the plotted line==================================
# axes.plot(x,y, color='purple', linewidth = 3)


# For blurring of the plotted line==================================
# axes.plot(x,y, color='purple', linewidth = 3, alpha=0.5)


# For line style of the plotted line==================================
# axes.plot(x,y, color='purple', linewidth = 3, linestyle="solid")
# axes.plot(x,y, color='purple', linewidth = 3, linestyle="dashed")
# axes.plot(x,y, color='purple', linewidth = 3, linestyle="dotted")
# axes.plot(x,y, color='purple', linewidth = 3, linestyle="dashdot")
# axes.plot(x,y, c='purple', lw = 3, ls=":")

# For marker and marker size, markerfacecolor of the plotted line
# axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o")
# axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", markersize = 10)

# axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", markersize = 10, markerfacecolor= 'g')
# axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", ms = 10, mfc= 'g')


# axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", ms = 10, mfc= 'g', markeredgewidth=3, markeredgecolor='red')
axes.plot(x,y, c='purple', lw = 3, ls="solid", alpha=0.5, marker="o", ms = 10, mfc= 'g', mew=3, mec='red')





# plt.tight_layout()
plt.show()