num1,num2,num3 = 4,6,5
numbers =[num1,num2,num3]

# print(f'Largest number is {max(numbers)} and Smallest number is {min(numbers)}')

if(num1 >= num2 and num1 >= num3): print(f'Largest number is {num1}')
elif(num2 >= num1 and num2 >= num3): print(f'Largest number is {num2}')
else : print(f'Largest number is {num3}')




'''
#For any numbers set: 

Limit = int(input('Enter how many elements : '))
numbers = []
for i in range(Limit):
    numbers.append(int(input(f'Enter a number at {i+1} position : ')))
if num not in numbers: #to check if list is not empty
    largest_num = numbers[0]
    for j in numbers[1:]:
        if j > largest_num:
            largest_num = j
else : print('The list is empty')
print(f"The Largest Number is {largest_num}")'''

