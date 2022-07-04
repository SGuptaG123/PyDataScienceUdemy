'''
    Most Popular Python Data science Libraries
    Numpy, Scipy, Pandas, Seaborn, Scikit-Learn, MatplotLib, Plotly, Pyspark and much more

'''


# While Loop ===============================

i = 0
while i < 5:
    print(f"The value of i is : {i}")
    i+=1

exit()

#  Functions =========================

def square_num(num):
    return num**2


print(square_num(16))


exit()


# List comprehension

mylist = [1,2,3,4,5,6]
out = []

for i in mylist:
    out.append(i**2)
print(out)


out2 = [x**2 for x in mylist]
print(out2)



exit()


print(list(range(0,20,2)))
print(list(range(20)))

for x in range(0,4):
    print(x)