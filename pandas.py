import pandas as pandas
print("pandas as successfully installed")


import pandas as pd
a  = (10,20,30,40,50)
s = pd.Series(a)
print(s)


import pandas as pd
a = ()
s = pd.Series(a)
print(s)
print(type(s))

import pandas as pd
m = [10,30,40,50,60]
s = pd.Series(m)
print(s)

import pandas as pd
m =[10,30,40,60,50,"name"]
s = pd.Series(m)
print(s)
print(type(s))



import pandas as pd
m = [10,30,40,50,50,60]
s = pd.Series(m,name = "Smarks")
print(s)


import pandas as pd
m = ["raju","karthik","praveen","vamshi"]
s = pd.Series(m,name = "students")
print(s)
print(type(s))


import pandas as pd
r = range(100)
a = list(r)
s = pd.Series(a)
print(s)

import pandas as pd
r = range(40)
a = list(r)
s = pd.Series(a,name = "prasad")
print(s)

import pandas as pd
m = (20,30,40,50,50,60,60)
for value in m:
    s = pd.Series(m)
    print(s)

import pandas as pd
import numpy as np
value = [10,20,30,40,50]
data  = np.array(value)
print(value)
print(data)
print(type(data))

import pandas as pd
import numpy as np
values = [10,20,30,40,50]
for value in values:
    print(values)

import pandas as pd
import numpy as np
values = [1,2,3,4,5,6]
s = pd.Series(values)
print(s)

import pandas as pd
import numpy as np
values = [1,2,3,4,5,6]
for value in values:
    print(value)
    print(type(value))

import pandas as pd
import numpy as np
values = ['a','b','c','d']
data = np.array(values)
s = pd.Series(data)
print(s)

import pandas as pd
import numpy as  np
values = ['a','b','c','d']
for value in values:
    print(value)
    print(type(value))

import pandas as pd
v = [12,34,5,55,44]
s = pd.Series(v)
print(s)


import pandas as pd
v=[1,2,3,4,5]
s = pd.Series(v,name = 'count')
print(s)

import pandas as pd
v = [1,2,3,4,5]
i = [10,20,30,40,50]
s = pd.Series(v,name = 'count',index = i)
print(s)

import pandas as pd
prices = [1000, 2000, 3000, 4000]
products = ["Nokia", "Samsung", "Oppo", "iPhone 6"]
s = pd.Series(prices, name = 'mobiles', index = products )
print(s)

import pandas as pd
v = [1,2,3,4,5]
s = pd.Series(v,name = "marks")
print(s)
print()
print(s[0])
print(s[1]) 

import pandas as pd
prices = [1000, 2000, 3000, 4000]
products = ["Nokia", "Samsung", "Oppo", "iPhone 6"]
s = pd.Series(prices, name = 'mobiles', index = products )
print(s)
print()
print(s["Nokia"])
print(s["Samsung"])


import pandas as pd 
import numpy as np
marks = [22,33,44,55,66]
s = pd.Series(marks)
print(s)


import pandas as pd
import numpy as np
marks = [1,22,44,55,66,88]
for value in marks:
    print(value)
    print(type(value))


import pandas as pd 
import numpy as np
names = ["raju","rajan","swathi",np.nan]
s = pd.Series(names)
print(s)

import pandas as pd
marks = [12,22,33,44,55]
s = pd.Series(marks)
print(s)
print(s.values)


import pandas as pd
names = ["raju","praveen","vamshi"]
s = pd.Series(names)
print(s)
print(s.values)

import pandas as pd
marks = [22,33,44,55,66]
s = pd.Series(marks)
print(s)
print(s.index)

import pandas as pd
marks = [56, 45, 35, 41, 44, 60]
i = [11, 12, 13, 14, 15, 16]
s = pd.Series(marks, index = i)
print(s)
print(s.index)


import pandas as pd
marks = [1,22,33,44,55,66]
i = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(marks, index = i)
print(s)
print(s.index)


import pandas as pd
marks = [1,34,6,77,88,99]
s = pd.Series(marks)
print(s)

import pandas as pd
salaries = [1000.23, 1100.45, 8889.7, 999.87]
s = pd.Series(salaries)
print(s)
print(s.dtypes)


import pandas as pd
names = ["Daniel", "Abhinav", "Dinesh", "Akshitha"]
s = pd.Series(names)
print(s)
print(s.dtypes)

import pandas as pd
marks = [56, 45, 35, 41, 44, 60]
s = pd.Series(marks)
print(s)

import pandas as pd
marks = [56, 45, 35, 41, 44, 60,55,90,80]
s = pd.Series(marks)
print(s)
print(s.head())


import pandas as pd
marks = [56, 45, 35, 41, 44, 60,90,88,78]
s = pd.Series(marks)
print(s)
print(s.tail())


import pandas as pd
sales = [56, 45, 35, 41, 44, 60]
s = pd.Series(sales)
print(s)
print(s.sum())


import pandas as pd
import numpy as np
marks = [56, 45, 35, 41, np.nan, 60, np.nan]
s = pd.Series(marks)
print(s)
print(s.sum())

import pandas as pd
import numpy as np
marks = [1,2,3,4,44,np.nan,60,np.nan]
s = pd.Series(marks)
print(s)
print(s.count())


import pandas as pd
sales = [10, 20, 30, 40, 50]
s = pd.Series(sales)
print(s)
print(s.mean())

import pandas as pd
sales = [10, 20, 30, 40, 50]
s = pd.Series(sales)
print(s)
print(s.describe())


import pandas as pd
sales = [10, 20, 30,40,40,40,40,50,50,50,50]
s = pd.Series(sales)
print(s)
print(s.unique())


import pandas as pd
sales = [10, 20, 30,40,40,40,40,50,50,50,50]
s = pd.Series(sales)
print(s)
print(s.nunique())



import pandas as pd
df = pd.DataFrame()
print(df)


import pandas as pd
a = [10, 20, 30,40,40,40,40,50,50,50,50]
df = pd.DataFrame(a)
print(df)
print(type(df))

import pandas as pd
names = ["raju","praveen","karthik","vishal"]
df = pd.DataFrame(names)
print(df)
print(type(df))


import pandas as pd
names = ["raju","praveen","karthik","vishal"]
df = pd.DataFrame(names)
print(df)
print(len(df))

import pandas as pd
details =[
           ["raju", 1],
           ["karthik", 2],
           ["praveen",3],
           ["mukesh",4],
           ["vishal",5],
           ["sumanth",6]
]
df = pd.DataFrame(details)
print(df)

import pandas as pd
details =[
           ["raju", 1,100],
           ["karthik", 2,200],
           ["praveen",3,300],
           ["mukesh",4,400],
           ["vishal",5,500],
           ["sumanth",6,600]
]
cols = ["Name","Age","Salary"]
df = pd.DataFrame(details,columns =cols)
print(df)


import pandas as pd
names = {
    "Name":["raju","praveen","karthik","vishal"],
     "Age" : [23,24,24,26]
}
df = pd.DataFrame(names)
print(df)




import pandas as pd
details = [
        ["Sagar", 20, 10000],
        ["Daniel", 16, 20000],
        ["Veeru", 24, 30000],
        ["Raju", 25, 40000],
        ["Kiran", 26, 50000],
        ["Kedar", 27, 60000],
        ["Reena", 28, 70000],
        ["Karthik", 29, 80000],
        ["Satish", 30, 90000]
]
c = ["Name","Age","Salary"]
i = [12,13,14,15,16,17,18,19,20]
df = pd.DataFrame(details,columns = c,index =i)
print(df)


import pandas as pd
details = [
        ["Sagar", 20, 10000],
        ["Daniel", 16, 20000],
        ["Veeru", 24, 30000],
        ["Raju", 25, 40000],
        ["Kiran", 26, 50000],
        ["Kedar", 27, 60000],
        ["Reena", 28, 70000],
        ["Karthik", 29, 80000],
        ["Satish", 30, 90000]
]
c = ["Name","Age","Salary"]
i = ["Row1", "Row2", "Row4", "Row5", "Row6", "Row7", "Row8",
"Row9", "Row10"]
df = pd.DataFrame(details, columns = c,index =i)
print(df)



import pandas as pd 
df = pd.read_csv("sales1.csv")
print(df)

import pandas as pd 
df = pd.read_csv("sales1234.csv")
print(df)


import pandas as pd
df = pd.read_csv('files\sales1.csv')
print(df)


import pandas as pd
df = pd.read_csv('D:\sales1.csv')
print(df)


import pandas as pd 
df = pd.read_json("sales1.json")
print(df)


import pandas as pd
df = pd.read_json("sales1234.json")
print(df)


