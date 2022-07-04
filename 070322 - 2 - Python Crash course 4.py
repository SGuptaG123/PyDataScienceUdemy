# Tuple Unpacking =======================

x = [(1,2),(3,4),(5,6)]
print(x[0][1])

for item in x:
    print(item)


for (a,b) in x:
    print(a)
    print(b)


exit()


# Strings ========================

s = "Hello my name is sandeep"
print(s.lower())
print(s.upper())
print(s.capitalize())

print(s.split())

tweet = "Go sports! #Sports"
sp = tweet.split('#')
print(sp)
print(sp[1])




exit()

# Built in Filter Function ====================

my_list2 = [x for x in range(0,21)]
print(my_list2)
myFilterList = list(filter(lambda num:num%2 ==0, my_list2))
print(myFilterList)


exit()

# Lambda Expression
T = lambda var:var*2
print(T(16))


my_list = [1,2,3,4,5]
map_list = list(map(lambda var:var**3, my_list))
print(map_list)



exit()


# Map function====================

def times2(var):
    return var*2


my_list = [1,2,3,4,5]

map_list = list(map(times2, my_list))

print(map_list)


