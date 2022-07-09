'''
    official website ->> Matplotlib.org/index.html


'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2


# Simple Plotting concept
# plt.plot(x,y,'g-')
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title("My first Plot chart")



# # Simple Plotting concept including SubPlots
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# plt.show()


# Using Object Oriented Methods
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes.set_title("My Title using OOPs method")


# Using Objec Oriented method with multiple SubPloting

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(x, y, 'r')
axes1.set_xlabel("X Label")
axes1.set_ylabel("Y Label")
axes1.set_title("Outer Plot")


axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axes2.plot(y, x, 'g')
axes2.set_xlabel("X Label")
axes2.set_ylabel("Y Label")
axes2.set_title("Inner Plot")

plt.show()



