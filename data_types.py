'''facts to be remembered 
SETS : represented by {}
1.Sets are Unordered collections of unique elements and Immutable. 
2.They only store values, not keys.
3.Once a set is created, you cannot change its items, but you can add new items.
4.Duplicates are not allowed.

TUPLES : represented by () ; It is Immutable, Ordered. 
DICTIONARY : represented by d = {'x' : 'yz'} and access the value by d['key']
'''

num1,num2 = 3,4.0
num3 = num1+4j

print(f'Num1 = {num1} is a type of {type(num1)}')
print(f'Num2 = {num2} is a type of {type(num2)}')
print(f'Num3 = {num3} is a type of {type(num3)}')

#create a list language with str
Languages = ['Python', 'Java', 'C++']
#print the str in the list Language of index 0
print(f'Currently iam learning {Languages[0]} programming')

#create a tuple of str and int
ide = ('Eclipse', 'Visual Studios', 123, 3.14)
#print the elements of tuple ide of index 1 and 3
print(f'Ide working on {ide[1]} and the version is {ide[3]}')

#create a set of employee id
employee_id = {123,234,345,456,567}
print(f'Employee id are {employee_id}')

#create a dictionary employee details
employee_details = {'Kaustubh' : 1234 , 'Ram' : 2345 , 'Krishna' :  3456 }
name1 = 'Kaustubh'
#print the value of key name1  from dictionary employee_details
print(f'employee id of {name1} is {employee_details[name1]}')