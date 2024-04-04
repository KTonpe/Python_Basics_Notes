'''
For checking the numner is even -> divide by 2 and find the remainder is 0 -> (% Modulo)
'''

# check number is Positive/Negative and Even/Odd
num = int(input("Enter a number to check if it is even or odd: "))
sign = 'Positive' if (num > 0) else 'Zero' if (num == 0) else 'Negative'
even_or_odd = 'Even' if (num % 2 == 0) else 'Odd'  #if else cond in single line
print(f'{num} is {sign} and {even_or_odd}')

# if num % 2 == 0:
#     print(f'Number {num} is Even')
# else :
#     print(f'Number {num} is Odd')

# if num> 0: print(f'Number {num} is Positive')
# elif num < 0: print(f'Number {num} is Negative')
# else: print(f'Number {num} is Zero')