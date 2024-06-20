'''
Import cmath to operate on complex numbers.
given condition (a != 0) to get the roots of quadratic
used if condition to check the at the earliest to save time
if true -> store the expression using f string in a variable
perform the operation
print the result
'''
import cmath

print('The quadratic expression is ax**2 + bx + c = 0')
a = float(input('Enter coefficiant of a : '))
#check if a is not equal to 0 or not
if(a != 0):
#perform this steps if a is not equal to 0

    b = float(input('Enter coefficiant of b : '))
    c = float(input('Enter coefficiant of c : '))
    
    expression = f'{a}x**2 + {b}x + {c} = 0'

    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print(f'Roots of {expression} are :  {sol1} and {sol2}')

#print this statement if a is equal to 0
else :
    print(f'Enter the value of a which is not equal to 0')


