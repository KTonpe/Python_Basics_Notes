'''
Python converts small data type to large to avoid loss of data
here FLOAT > INTEGER

IMPLICIT conversion will not cause loss of data
EXPLICIT conversion may cause loss of data due to manually changing the datatype

Float holds upto 15 places

Binary is base 2 (0b) / Hexadecimal  is base 16 (0x) / Octal  is base 8 (0o)
'''

num1_integer = 5
num2_float = 3.14
Sum = num1_integer + num2_float
#Implicit type casting
print(f'\nSum of {num1_integer} and {num2_float} is : {Sum} and the data-type is {type(Sum)}')

#Explicit Type Cast for Float (3.14 -> 3)
Sum = num1_integer + int(num2_float) 
print(f'\nSum of {num1_integer} and int of {num2_float} is : {Sum} and the data-type is {type(Sum)} \n')

num3_as_String = '45'
print(f'Datatype of {num3_as_String} is {type(num3_as_String)}')
print(f'Datatype of {num1_integer} is {type(num1_integer)}')
print(f'Datatype of {num2_float} is {type(num2_float)}')

#Explicit typecasting = convert str to int to perfom addition
num3_as_String = int(num3_as_String)
Sum = num1_integer + num3_as_String
print(f'\nAddition of {num1_integer} and {num3_as_String} is {Sum} and the data-type is {type(Sum)} \n')

#print(binary,hexa,octal)
print(0b1101011,(0xFB + 0b10),0o15)




