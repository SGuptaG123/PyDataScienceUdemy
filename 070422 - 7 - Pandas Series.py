import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4],['USA', 'UK', 'Germany', 'Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA', 'USSR', 'Italy', 'Japan'])
print(ser2)

print(ser1 + ser2)

exit()

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

print(labels)
print(my_data)
print(arr)
print(d)


print(pd.Series(labels))
print(pd.Series(my_data))
print(pd.Series(data=my_data, index=labels)) 
print(pd.Series(d))


