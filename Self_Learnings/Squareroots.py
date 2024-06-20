'''
Importing cmath to operate on complex numbers

eval() function is used to execute a string containing Python code.
it evaluates that string as a Python expression, statement, or code block. 
ex: x,y = 1,2
    code_string = 'x + y'
    reult = eval(code_string) --> result = 1 + 3 (String to expression)
    print(result) = 3
'''

# Importing the complex math module
import cmath

num1 = float(input("enter a number to find its squareroot : "))
#num1 ** 0.5 -> Return float
print(f'Square root of the number {num1} is {num1 ** 0.5}')


complex_num = eval(input('Enter a complex number to find its square root : '))
complexnum_sqrt = cmath.sqrt(complex_num)
#print(type(complexnum_sqrt)) -> returns complex in ()
print(f'Square root of the number {complex_num} is {complexnum_sqrt.real} + {complexnum_sqrt.imag}j')
