import numpy as np
s= lambda x,y:x+y
gt = lambda x,y : x if x>y else y
e_o = lambda x : True if x%2 == 0 else False

print("sum is (3,4) : ",s(3,4))
print("Greater (3,4) is : ",gt(3,4))
print("3 is : ",e_o(3))

li =[1,2,3,4,5,6,7,8,88]
even_list = list(filter(lambda x :x%2 == 0,li))
print(even_list)

squared_list_formula = lambda x :x**2
squared_list = list(map(squared_list_formula,li))
print(squared_list)

nump_li = np.array(li)

print(nump_li)
print(nump_li.mean())
print(nump_li**2)
even_nump_list = nump_li[nump_li % 2 == 0]
print(list(even_nump_list))