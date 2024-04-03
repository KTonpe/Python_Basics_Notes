num1 = float(input('Enter a number at place 1 : '))
num2 = float(input('Enter a number at place 2 : '))

print(f'Numbers before swapping are num1 = {num1} and num2 = {num2}.')

#without using extra variable "temp"
num1,num2 = num2,num1
print(f'Numbers after swapping are num1 = {num1} and num2 = {num2}.')

'''
#using XOR : (1^1 = 0 ; 1^0 = 1 , 0^1 = 1 , 0^0 = 0)
#Before swapping num1 = 1 and num2 = 2
num1 = num1 ^ num2      #num1 = 01 ^ 10 = 11 -> 3
num2 = num1 ^ num2      #num2 = 11 ^ 10 = 01 -> 2
num1 = num1 ^ num2      #num1 - 11 ^ 01 = 10 -> 1
print(f'Numbers after swapping are num1 = {num1} and num2 = {num2}.')

#using addition and subtraction:
#Before swapping num1 = 1 and num2 = 2
num1 = num1 + num2      #num1 = 1 + 2 = 3
num2 = num1 - num2      #num2 = 3 - 2 = 1
num1 = num1 - num2      #num1 = 3 - 1 = 2
#After swapping is num1 = 2 and num2 = 1
print(f'Numbers after swapping are num1 = {num1} and num2 = {num2}.')

#Using a variable temp :
temp = num1
num1 = num2
num2 = temp
print(f'Numbers after swapping are num1 = {num1} and num2 = {num2}.')
'''

