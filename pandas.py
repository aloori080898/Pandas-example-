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
import pandas as pd
df = pd.read_csv("sales1.csv")
print(df.Product)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
s = df["Product"]
print(s)


import pandas as pd
df1 = pd.read_csv("sales1.csv")
cols = ["Customer Name", "Product"]
df2 = df1[cols]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
total = df1["Quantity"].sum()
print(total)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
print(df1)

import pandas as pd
df1 = pd.read_csv("sales1.csv")
cust_name = df1["Product"] == "Veeru"
print(df1[cust_name])

import pandas as pd
df1 = pd.read_csv("sales1.csv")
cust_name = df1["Customer Name"] == "Veeru"
print(df1[cust_name])

import pandas as pd
df1 = pd.read_csv("sales1.csv")
prod_name = df1["Product"] == "Macbook Pro Laptop"
print(df1[prod_name])

import pandas as pd
df1 = pd.read_csv("sales1.csv")
cust_name = df1["Product"] == "Prasad"
print(df1[cust_name])

import pandas as pd
df1 = pd.read_csv("sales2.csv")
print(df2)


import pandas as pd
df1 = pd.read_csv("sales2.csv")
print(df1)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[0]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[1]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[2]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[-1]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[-2]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc["Order id"]
print(s)


import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,0]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,1]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,2]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,4]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,6]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,-1]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[0:5]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,0:2]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,0:3]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,0:4]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[:,0:-1]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[0:5,0:2]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[0:5,0:3]
print(s)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
s = df1.iloc[0:5,0:4]
print(s)


import pandas as pd
df1 = pd.read_csv("sales2.csv")
print(df1)

import pandas as pd
df1 = pd.read_csv("sales2.csv")
df1.set_index("Product name", inplace = True)
print(df1)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace =True)
a = 'iPhone 9'
df2 = df1.loc[a]
print(df2.head(10))

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace =True)
a = 'ThinkPad Laptop'
df2 = df1.loc[a]
print(df2.head(10))

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['iPhone 9', 'iPhone 11']
df2 = df1.loc[a]
print(df2)


import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['ThinkPad Laptop', '27in FHD Monitor']
df2 = df1.loc[a]
print(df2)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['iPhone 9', 'ThinkPad Laptop']
b = ['Product cost', 'Customer id']
df2 = df1.loc[a, b]
print(df2)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['iPhone 9', 'ThinkPad Laptop']
b = ['Product cost', 'Customer name']
df2 = df1.loc[a, b]
print(df2)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['iPhone 8', 'Google Phone']
df2 = df1.loc[a, 'Order id' : 'Product cost']
print(df2)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
df1.set_index("Product name", inplace = True)
a = ['iPhone 8', 'Google Phone']
df2 = df1.loc[a, 'Order id' : 'Customer id']
print(df2)

import pandas as pd
df1 = pd.read_csv('sales2.csv')
a = df1['Product name'] == 'LG Washing Machine'
df2 = df1.loc[a]
print(df2.head())

import pandas as pd
df1 = pd.read_csv('sales2.csv')
a = df1['Product name'] == 'LG Washing Machine'
df2 = df1.loc[a, 'Order id' : 'Product cost']
print(df2.head())

import pandas as pd
df1 = pd.read_csv('sales2.csv')
a = df1['Customer name'] == 'Sagar'
df2 = df1.loc[a, 'Product name' : 'Product cost']
print(df2.head())

import pandas as pd
df = pd.read_csv("sales4.csv")
print(df)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1['Product_Cost'] > 65000
df2 = df1[con1]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1['Product_Cost'] > 70000
df2 = df1[con1]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1['Product_Cost'] > 50000
con2 = df1['Product_Cost'] < 60000
df2 = df1[con1 & con2]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1.Product_Name == "iPhone 11"
con2 = df1.Customer_Name == "Nireekshan"
df2 = df1[con1 & con2]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1.Product_Name == "iPhone 11"
con2 = df1.Customer_Name == "Shahid"
df2 = df1[con1 & con2]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
con1 = df1.Product_Name == "iPhone 11"
con2 = df1.Customer_Name == "Shahid"
df2 = df1.loc[con1 & con2]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.iloc[:5, ]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
rows = df1.index[0:]
cols = ["Product_Name", "Customer_Id"]
df2 = df1.loc[rows, cols]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
rows = df1.index[0:4]
cols = ["Product_Name", "Customer_Id"]
df2 = df1.loc[rows, cols]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
rows = df1.index[5:]
cols = ["Product_Name", "Customer_Id"]
df2 = df1.loc[rows, cols]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
a = df1.Product_Name == "LG Washing Machine"
b = df1.Customer_Id == 1
c = a | b
df2 = df1.loc[c]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
a = ["Macbook Pro Laptop"]
b = df1.Product_Name.isin(a)
df2 = df1[b]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
a = ["Macbook Pro Laptop"]
b = df1.Product_Cost.isin(a)
df2 = df1[b]
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
a = ["34in Ultrawide Monitor", "Macbook Pro Laptop"]
b = df1.Product_Name.isin(a)
df2 = df1[b]
print(df2)

import pandas as pd
df = pd.read_csv("sales4.csv")
a = pd.unique(df.Product_Name)
print(a)
print(len(a))

import pandas as pd
df = pd.read_csv("sales4.csv")
a = pd.unique(df.Customer_Name)
print(a)
print(len(a))

import pandas as pd
import numpy as np
data = [
['Shahid', 21, 40000],
['Nireekshan', 22, 20000],
['Veeru', 45, 90000],
['Sumanth', 20, 95000],
[np.nan, 2, 99000],
['Prasad', 1, 41000]
]
c = ['Name', 'Age', 'Salary']
df1 = pd.DataFrame(data, columns = c)
print(df1)


import pandas as pd
import numpy as np
data = [
['Shahid', 21, 40000],
['Nireekshan', 22, 20000],
['Veeru', 45, 90000],
['Sumanth', 20, 95000],
[np.nan, 2, 99000],
['Prasad', 1, 41000]
]
c = ['Name', 'Age', 'Salary']
df1 = pd.DataFrame(data, columns = c)
d = df1.Name.notnull()
df2 = df1[d]
print(df1)
print()
print(df2)

import pandas as pd
df = pd.read_csv("sales4.csv")
print(df)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Product_Cost")
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Product_Cost")
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Customer_Id")
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Customer_Id", ascending = False)
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Customer_Id", ascending = 0)
print(df2)

import pandas as pd
df1 = pd.read_csv("sales4.csv")
df2 = df1.sort_values(by = "Customer_Name")
print(df2)

import pandas as pd
d = {
'Order id': [11, 21, 31],
'Customer name': ['Kedar', 'Nireekshan', 'Daniel'],
'Product': ['iPhone 11','hTC', 'macbook']
}
i = [555, 444, 333]
df1 = pd.DataFrame(d, index = i)
df2 = df1.sort_index()
print(df1)
print()
print(df2)

     import pandas as pd
d = {
"Product": ["Samsung", "Nokia", "Samsung", "Motorola",
"Nokia", "Samsung", "Samsung"],
"Orders": [2, 4, 3, 4, 6, 7, 3]
}
df1 = pd.DataFrame(d)
print(df1)

import pandas as pd
d = {
"Product": ["Samsung", "Nokia", "Samsung", "Motorola",
"Nokia", "Samsung", "Samsung"],
"Orders": [2, 4, 3, 4, 6, 7, 3]
}
df1 = pd.DataFrame(d)
grouped = df1.groupby(["Product"])
result = grouped.sum()
print(df1)
print()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
grouped = df1.groupby(["Mail_Id"])
result = grouped.size()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
grouped = df1.groupby(["Product_Name"])
result = grouped.size()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Product_Name','Date']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Mail_Id', 'Date']
grouped = df1.groupby(cols)['Mail_Id']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id', 'Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id','Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id','Product_Name']
grouped = df1.groupby(col,as_index = False)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Date']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Cost'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Name'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum,
'Product_Name': "count"
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : ['min','max','sum']
}
cols = ['Product_Cost']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
grouped = df1.groupby(["Product_Name"])
result = grouped.size()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Product_Name','Date']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Mail_Id', 'Date']
grouped = df1.groupby(cols)['Mail_Id']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id', 'Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id','Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id','Product_Name']
grouped = df1.groupby(col,as_index = False)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Date']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Cost'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Name'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum,
'Product_Name': "count"
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : ['min','max','sum']
}
cols = ['Product_Cost']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
grouped = df1.groupby(["Product_Name"])
result = grouped.size()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Product_Name','Date']
grouped = df1.groupby(cols)['Date']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
cols = ['Mail_Id', 'Date']
grouped = df1.groupby(cols)['Mail_Id']
result = grouped.count()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id', 'Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col = ['Mail_Id','Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id','Product_Name']
grouped = df1.groupby(col,as_index = False)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Mail_Id']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Product_Name']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
col =['Date']
grouped = df1.groupby(col)['Product_Cost']
result = grouped.sum()
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Cost'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
df2 = df1['Product_Name'].describe()
print(df2)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : sum,
'Product_Name': "count"
}
cols = ['Date', 'Product_Name']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)


import pandas as pd
df1 = pd.read_csv("sales5.csv")
d = {
'Product_Cost' : ['min','max','sum']
}
cols = ['Product_Cost']
grouped = df1.groupby(cols)
result = grouped.agg(d)
print(result)

import pandas as pd
d1 = {
"Id": [1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan",
"Shafi", "Veeru"],
"Subject": ["English", "Java", "Html", "Python", "C", "dotnet"]
}
d2 = {
"Id": [11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject": ["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
print(df1)
print()
print(df2)

import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan",
"Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dotnet"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
inn_join = pd.merge(df1, df2, on = "Subject", how = "inner")
print(df1)
print()
print(df2)
print()
print(inn_join)

import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan",
"Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dotnet"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
left_join = pd.merge(df1, df2, on = "Subject", how = "left")
print(df1)
print()
print(df2)
print()
print(left_join)

import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan",
"Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dotnet"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
right_join = pd.merge(df1, df2, on = "Subject", how = "right")
print(df1)
print()
print(df2)
print()
print(right_join)

import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan",
"Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dotnet"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
outer_join = pd.merge(df1, df2, on = "Subject", how = "outer")
print(df1)
print()
print(df2)
print()
print(outer_join)

import pandas as pd
d1 = {
"Employee": ["Nireekshan", "Veeru", "Lavanya", "Pradhan"],
"Group": ["Development", "Testing", "Testing", "HR"]
}
d2 = {
"Employee": ["Lavanya", "Nireekshan", "Veeru", "Pradhan"],
"Hire_date": [2010, 2012, 2014, 2016]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
one_one = pd.merge(df1,df2)
print(df1)
print()
print(df2)
print()
print(one_one)

import pandas as pd
d1 = {
"Employee": ["Nireekshan", "Veeru", "Lavanya", "Pradhan"],
"Group": ["Development", "Testing", "Testing", "HR"]
}
d2 = {
"Employee": ["Lavanya", "Nireekshan", "Veeru", "Pradhan"],
"Hire_date": [2010, 2012, 2014, 2016]
}
d3 = {
"Group": ["Testing", "Development", "HR"],
"supervisor": ["Shafi", "Daniel", "Neelima"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)
one_one = pd.merge(df1,df2)
many_one = pd.merge(one_one,df3)
print(df1)
print()
print(df2)
print()
print(many_one)

import pandas as pd
d1 = {
"Employee": ["Nireekshan", "Veeru", "Lavanya", "Pradhan"],
"Group": ["Development", "Testing", "Testing", "HR"]
}
d2 = {
"Group": ["Testing", "Testing", "Development","Development", "HR", "HR"],
"Skills": ["Manual", "Automation", "Coding", "Logical","Spreadsheets", "Organization"]
}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
many_many = pd.merge(df1, df2)
print(df1)
print()
print(df2)
print()
print(many_many)


import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan","Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dott"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
result =  pd.merge(df1,df2, on = "Subject")
print(df1)
print()
print(df2)
print()
print(result)

import pandas as pd
d1 = {
"Id":[1, 2, 3, 4, 5, 6],
"Name": ["Pradhan", "Venu", "Madhurima", "Nireekshan","Shafi", "Veeru"],
"Subject":["English", "Java", "Html", "Python", "C", "dott"]
}
d2 = {
"Id":[11, 12, 13, 14, 15, 16],
"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun",
"Veeru"],
"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
result =  pd.merge(df1,df2, on = ["Subject","Name"])
print(df1)
print()
print(df2)
print()
print(result)

import pandas as pd 
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c1)
print(df1)
print()
print(df2)

import pandas as pd 
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c1)
result = [df1,df2]
print(df1)
print()
print(df2)
print()
print(result)

import pandas as pd 
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c1)
result = [df1,df2]
df3 = pd.concat(result)
print(df1)
print()
print(df2)
print()
print(df3)

import pandas as pd 
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c1)
result = [df1,df2]
df3 = pd.concat(result,ignore_index = True )
print(df1)
print()
print(df2)
print()
print(df3)

import pandas as pd 
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c1)
result = [df1,df2]
df3 = pd.concat(result,ignore_index = False )
print(df1)
print()
print(df2)
print()
print(df3)

import pandas as pd
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
c2 = ["X", "Y"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c2)
print(df1)
print()
print(df2)

import pandas as pd
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
c2 = ["X", "Y"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c2)
result = [df1, df2]
df3 = pd.concat(result, axis = 1)
print(df1)
print()
print(df2)
print()
print(df3)

import pandas as pd
d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]
c1 = ["A", "B"]
c2 = ["X", "Y"]
df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c2)
result = [df1, df2]
df3 = pd.concat(result, ignore_index = True )
print(df1)
print()
print(df2)
print()
print(df3)

import pandas as pd
df = pd.read_csv("sales8.csv")
print(df.head(5))

import pandas as pd
df = pd.read_csv("sales8.csv")
df['Status'] = "Delivered"
print(df.head())

import pandas as pd
df = pd.read_csv("sales8.csv")
df["Total Cost"] = df['Product cost']*df['Quantity']
print(df.head(5))

import pandas as pd
df = pd.read_csv("sales8.csv")
def total(df):
    t = df['Product cost'] * df['Quantity']
    return t
df['Total cost'] = df.apply(total, axis = 1)
print(df.head())

import pandas as pd
df = pd.read_csv("sales8.csv")
print(df.head())
new = df['Product cost'] * df['Quantity']
df.insert(5,"Total Cost", new)
print()
print(df.head(5))

import pandas as pd
df1 = pd.read_csv("sales8.csv")
df2 = df1.drop(columns = 'Customer name')
print(df1.head())
print()
print(df2.head())

import pandas as pd
df1 = pd.read_csv("sales8.csv")
df2 = df1.drop(['Customer name', 'Product name'], axis = 1)
print(df1.head())
print()
print(df2.head())

import pandas as pd
df1 = pd.read_csv("sales8.csv")
df2 = df1.drop(3, axis = 0)
print(df1.head())
print()
print(df2.head())

import pandas as pd
df1 = pd.read_csv("sales8.csv")
df2 = df1.drop([1, 2], axis = 0)
print(df1.head())
print()
print(df2.head())

import os
path = "./daniel"
all_files = os.listdir(path)
print(all_files)

import os
path = "./daniel"
all_files = os.listdir(path)
f = filter(lambda name: name.endswith('.csv'), all_files)
csv_files = list(f)
print(all_files)
print()
print(csv_files)

import os
import glob
import pandas as pd
p = '.\daniel'
files = os.path.join(p, "*.csv")
csv_files = glob.glob(files)
result = (pd.read_csv(every) for every in csv_files)
df = pd.concat(result, ignore_index = True)
print(df)
df.to_csv("year.csv", index = False)

import pandas as pd
df = pd.read_csv("year.csv", parse_dates = ["Date"])
print(df)
