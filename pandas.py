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

import pandas as pd
df = pd.read_excel("sales1.xlsx")
print(df)

import pandas as pd
df = pd.read_table("sales1.tsv")
print(df)


import pandas as pd
url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'
df_list = pd.read_html(url)
print(df_list[2])

import pandas as pd
df = pd.read_csv("sales1.csv")
print("Total number of rows in DataFrame:", len(df))


import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.columns)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.shape)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.shape[0])

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.shape[1])

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.size)

import pandas as pd
df = pd.read_csv("sales1.csv")
print("Number of elements in DataFrame:", df.size)

import pandas as pd
df = pd.read_csv("sales1.csv")
print("Number of elements in DataFrame:", df.size)
print("Number of elements in DataFrame:",df.shape[0]*df.shape[1])

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.dtypes)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.empty)

import pandas as pd
df = pd.DataFrame()
print(df)
print()
print(df.empty)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.index)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.values)


import pandas as pd
details = [["Sagar", 20, 10000], ["Daniel", 16, 20000], ["Veeru", 24,
30000], ["Raju", 25, 40000], ["Kiran", 26, 50000], ["Kedar", 27,
60000], ["Reena", 28, 70000]]
df = pd.DataFrame(details, columns = ["Name", "Age", "Salary"])
print(df)
print()
print(df.T)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
df2 = df1.head()
print(df2)


import pandas as pd
df1 = pd.read_csv("sales1.csv")
df2 = df1.tail()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
df1.info()

import pandas as pd
df1 = pd.read_csv("sales1_with_nan.csv")
df1.info()

import pandas as pd
df1 = pd.read_csv("sales1.csv")
c = df1.count()
print(c)


import pandas as pd
df1 = pd.read_csv("sales1_with_nan.csv")
c = df1.count()
print(c)


import pandas as pd
df1 = pd.read_csv("sales1.csv")
df2 = df1.describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
df2 = df1.nunique()
print(df2)


import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.Product)

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df["Product"])

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df[["Customer Name", "Product"]])


import pandas as pd
df = pd.read_csv("sales1.csv")
total = df['Quantity'].sum()

import pandas as pd
df = pd.read_csv("sales1.csv")
print(df)

import pandas as pd
df = pd.read_csv("sales1.csv")
df = df[["Product", "Customer Name", "Quantity", "Order ID"]]
print(df)

import pandas as pd
df = pd.read_csv("sales3.csv")
print(df.head())
print()
print(df.columns)

import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {
"ord id": "Order Id"
}
df2 = df1.rename(columns = d)
print(df1.head())
print()
print(df2.head())


import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {
"orddddd id": "Order Id"
}
df2 = df1.rename(columns = d)
print(df1.head())
print()
print(df2.head())


import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {
'ord id': 'Order Id',
'cust name': 'Customer Name',
'cust id': 'Customer Id',
'prod name': 'Product Name',
'prod cost': 'Product Cost'
}
df2 = df1.rename(columns = d)
print(df1.head())
print()
print(df2.head())

import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {
"ord id": "order_id",
"cust name": "customer_name",
"cust id": "customer_id",
"prod name": "product_name",
"prod cost": "product_cost"
}
df2 = df1.rename(columns = d)
print(df1.head())
print()
print(df2.head())


import pandas as pd
df1 = pd.read_csv("sales3.csv")
print(df1.head())
df1.columns = [
"order_id",
"customer_name",
"customer_id",
"product_name",
"product_cost"
]
print()
print(df1.head())


import pandas as pd
df1 = pd.read_csv("sales3.csv")
print(df1.head())
df1.columns = [
"order_id",
"customer_name",
"customer_id",
"product_name",
"product_cost",
"total"
]
print()
print(df1.head())


import pandas as pd
d = {
"order_id": [11, 21, 31],
"customer_name": ["Prasad", "Daniel", "Jeswanth"],
"product": ["iPhone", "hTC", "macbook"]
}
df1 = pd.DataFrame(d)
print(df1)

import pandas as pd
d = {
"order_id": [11, 21, 31],
"customer_name": ["Prasad", "Daniel", "Jeswanth"],
"product": ["iPhone", "hTC", "macbook"]
}
i = {0: 77, 1: 88, 2: 99}
df1 = pd.DataFrame(d)
df2 = df1.rename(index = i)
print(df1)
print()
print(df2)


import pandas as pd
d = {
"order_id": [11, 21, 31],
"customer_name": ["Prasad", "Daniel", "Jeswanth"],
"product": ["iPhone", "hTC", "macbook"]
}
df1 = pd.DataFrame(d)
print(df1)
df1.index = [77, 88, 99]
print()
print(df1)


import pandas as pd
df1 = pd.read_csv("sales31.csv")
print(df1)
df1.index = range(10, 20)
print()
print(df1)


import pandas as pd
d = {
"Ord Id": [11, 21, 31],
"Customer Name": ["Prasad", "Daniel", "Jeswanth"],
"Product": ["iPhone", "hTC", "macbook"]
}
df1 = pd.DataFrame(d)
print(df1)
df1.index = [333, 444, 555]
df1.columns = ["order_id", "customer_name", "product"]
print()
print(df1)

import pandas as pd
df1 = pd.read_csv("sales3.csv")
print(df1.head())
df1.columns = df1.columns.str.upper()
print()
print(df1.head())


import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {"ord id": "order_id", "cust name": "customer_name", "cust
id": "customer_id", "prod name": "product_name", "prod cost":
"product_cost"}
print(df1.head())
df1.rename(columns = d)
print()
print(df1.head())

import pandas as pd
df1 = pd.read_csv("sales3.csv")
d = {"ord id": "order_id", "cust name": "customer_name", "cust
id": "customer_id", "prod name": "product_name", "prod cost":
"product_cost"}
print(df1.head())
df1.rename(columns = d, inplace = True)
print()
print(df1.head())


import pandas as pd
df1 = pd.read_csv("sales1_with_nan.csv")
c = df1.count()
print(c)

import pandas as pd
df = pd.read_csv("fruits1.csv")
print(df)

import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 = df1.isna()
print(df1)
print()
print(df2)

import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df2 =df1.notnull()
print(df1)
print()
print(df2)

import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 =df1.isnull().sum()
print(df1)
print()
print(df2)


import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 = df1.isnull().sum()
per = (df2*100)/len(df1)
print(per)

import pandas as pd
df1 = pd .read_csv("fruits1.csv")
s = df1.isnull().sum()
per = (s*100)/len(df1)
print(per)

import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 = df1.dropna()
print(df2)

import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 = df1.dropna()
s= df2.isnull().sum()
print(s)

import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df2= df1.dropna()
df3 = df2.astype(int)
print(df2)
print()
print(df3)

import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df2= df1.dropna()
df3 = df2.astype(int)
print(df2.head())
print()
print(df3.head())



import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df1.dropna(inplace = True)
df2 = df1.astype(int)
print(df2)

import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df1.dropna(inplace = True)
df2 = df1.astype(int)
print(df1.head())
print(df2.head())

import pandas as pd
df1 = pd.read_csv("fruits1.csv")
df2 = df1.fillna(0)
print(df2)

import pandas as pd
df1 =pd.read_csv("fruits1.csv")
df2 = df1.fillna(0)
df3 = df2.astype(int)
print(df2.head())
print()
print(df3.head())

import pandas as pd
import numpy as np
data = [
    ["Rajan", 26, 40000],
    ["Daniel", 16, 20000],
    ["Veeru", 45, 90000],
    ["Venkat", np.nan, 45000],
    ["Sumanth", 20, 95000],
    ["Shafi", np.nan, 97000]
]
df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Salary'])
df2 = df1.fillna(0)
print(df1)
print()
print(df2)


import pandas as pd
import numpy as np
data = [
["Rajan", 26, 40000],
["Daniel", 16, 20000],
["Veeru", 45, 90000],
["Venkat", np.nan, 45000],
["Sumanth", 20, 95000],
["Shafi", np.nan, 97000]
]
df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Salary'])
df2 = df1.fillna(22)
print(df1)
print()
print(df2)

import pandas as pd
import numpy as np
data = [
["Rajan", 26, 40000],
["Daniel", 16, 20000],
["Veeru", 45, 90000],
["Venkat", np.nan, 45000],
["Sumanth", 20, 95000],
["Shafi", np.nan, 97000]
]
df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Salary'])
a = df1['Age'].mean()
df1['Age'] = df1['Age'].fillna(a)
print()
print(df1)

import pandas as pd
import numpy as np
data = [
    ['Shahid', np.nan, 40000],
    ['Daniel', 16, 20000],
    ['Veeru', 45, 90000],
    ['Sumanth', 20, 95000]
 ]
df1 = pd.DataFrame(data, columns = ['Name', 'Age', 'Salary'])
print(df1)
df2 = df1.replace(np.nan, 0)
print()
print(df2)


import pandas as pd
df1 = pd.read_csv("sales1.csv")
print(df1.product)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
print(df1.Product)
per = (df1*100)/len(df1)
print(per)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
a = df1["Product"]
print(a)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
cols =["Customer Name","Product"]
df2 = df1[cols]
print(df2)


import pandas as pd
df1 = pd.read_csv("sales1.csv")
total =df1["Quantity"].sum()
print(total)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
print(df1)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
cust_name = df1["Customer Name"] == "Veeru"
print(df1[cust_name])


