import numpy as np

arr_2D = np.arange(50).reshape(5,10)
print(arr_2D)
print(arr_2D[1:3,3:5])


exit()

import numpy as np

arr = np.arange(1,11)
print(arr)
bool_arr = arr > 5
print(bool_arr)

print(arr[bool_arr])

print(arr[arr < 3])





exit()



import numpy as np

arr_2D = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2D)

print(arr_2D[1][1])
print(arr_2D[2][1])
print(arr_2D[2,1])

print(arr_2D[2,0:2])
print(arr_2D[:2,0:2])










exit()

'''
    Numpy Indexing and Selection
'''

import numpy as np

arr = np.arange(0,11)
print(arr)
print(arr[0:5])
print(arr[:6])
print(arr[5:])

arr[0:5] = 100
print(arr)