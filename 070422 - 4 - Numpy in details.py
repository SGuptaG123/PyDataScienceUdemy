'''
    np.array, np.arrange, np.zeros, np.ones, np.linspace, np.eye, np.random.rand, np.random.rndn, np.random.rndint
    
    .reshape(), .min(), .max(), .argmin(), .argmax()

'''


import numpy as np

mylist = [1,2,3,4,5]

arr = np.array(mylist)
print(type(arr))

print('\nList Conversion into Array')
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(my_mat)
print(arr2)


print('\nArray through Arrange')
print(np.arange(0,11,2))

print('\nArray through Zeros')
print(np.zeros(3))
print(np.zeros((2,5)))

print('\nArray through Ones')
print(np.ones((2,3)))


print('\nArray through Linspace')
print(np.linspace(0,5, 20))


print('\nArray through Random Eye')

print(np.eye(10))


print('\nArray through rand')
print(np.random.rand(5))
print(np.random.rand(5,5))

print('\nArray through randn')
print(np.random.randn(4,4))

print('\nArray through randint')
print(np.random.randint(low=2,high=100, size=(2,3)))

print('\nExercise Begins here..')
arr = np.arange(25)
print(arr)
print(arr.reshape(5,5))



print('\n\n Exerciese about Random integers: \n')
randarr = np.random.randint(0,50,10)
print(randarr)
print(randarr.max())
print(randarr.min())
print(randarr.argmax())
print(randarr.argmin())

print(randarr.dtype)