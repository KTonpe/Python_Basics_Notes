number = int(input('Enter a number to find its Factorial : '))

#factotial using RECURSION:
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1) #calling the factorial function again with decrementing x

if number < 0 : print(f'{number} Negative numbers can\'t have a factorial')
elif number == 0 : print(f'{number}! = 1') 
else : print(f'{number}! = {factorial(number)}')


'''# #factorial using loop
if number < 0 : print('Factorial doesn\'t exist for negative numbers')
elif number == 0: print(f'{number}! = 0 ')
else:
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    print(f'{number}! = {factorial}')'''