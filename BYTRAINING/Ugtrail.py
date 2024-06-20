#take input here
import ast 
import numpy as np
input_list=ast.literal_eval(input())
m=int(input())
n=int(input())

array_1 = np.array(input_list)#start writing your code from here
final_array = array_1 [ (array_1 > m) & (array_1 < n) ] #start writing your code from here

print(list(final_array))