'''
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
Always start with (first) a = 0 and (second) b = 1. 
The next number in the sequence is obtained by adding up the two numbers before it. -> next = a+b
print from 'a' -> to start the series from 0

Used WHILE LOOP because of the condition i < limit.
other wise in for loop we have to add if else cause in the loop to check

last one is Using RECURSIVE calling the function inside it 
the memory allocation for [for,while,do while] is minimal and 
for recurssive it involves stack space -> depends on the depth and variable
sometime it may lead to Stack Overflow if it exceeds size limit.


'''

limit = int(input('Enter the limit: '))

a,b = 0,1
i = 0

if limit < 0 or limit == 0 : print('Enter Positive number')
# else: 
#     print(f'Fibonacci numbers till {limit} terms are: ')
#     while i < limit :
#         print(a,end = ', ')
#         next = a + b
#         a,b= b,next 
#         i += 1

# till_number = int(input('Enter the number from fibonaci seq: '))
# a,b = 0,1
# if till_number <=    0: print('Enter valid number from seq')
# else:
#     print(f'Fibonacci series till the {till_number} are : ')
#     while a <= till_number:
#         print(a,end = ', ')
#         next = a + b
#         a,b= b,next

'''
#USING RECURSIVE FUNCTION: -> chatgpt
def fibonacci(n):
    if n <= 1: #this condition will append 0 and 1 to the list at the beginning
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

till_number = int(input('Enter the number from Fibonacci seq: '))

if till_number <= 0:
    print('Enter a valid number from seq')
else:
    fibonacci_sequence = []
    for i in range(till_number):
        fib_number = fibonacci(i)
        if fib_number <= till_number:
            fibonacci_sequence.append(fib_number)
        else:
            break

    print(', '.join(map(str, fibonacci_sequence)))
    '''

