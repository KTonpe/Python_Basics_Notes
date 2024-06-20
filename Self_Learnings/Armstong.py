'''
if (34) == (3x3 + 4x4) then it is armstrong
LOGIC :  same logic as reversing a number 
1. get the remainder by module -> remainder = number % 10 [Last digit or UNITS PLACE]
2. adding numbers = (adding numbers*10) + remainder [INCREMENT the digit to Tens and hundreds ..etc]
3. number without remainder -> number // 10 

Here to in the case of ARMSTRONG adding numbrs would cahnge to
adding numbers = remainder**(length of numbrs)
and check tht adding numbers with the actual number


from generating from the given length
we need start_range = 10**(length of numbrs-1)
'''

#to check wheather the number is a Armstrong number or not.
number = input("Enter a number : ")
temp = int(number)
sum_of_numbers = 0

while temp > 0:
    digit = temp%10
    sum_of_numbers += digit**len(number)
    temp //= 10
print(f'{number} is an Armstrong') if sum_of_numbers == int(number) else print(f'{number} is not a Armstrong')


#genrating an amstrong number of given length
length_of_number = int(input('Enter the length of a number : ')) #2
start_range = 10**(length_of_number-1) #10**(2-1) = 10 IMPLICIT
end_range = 10**(length_of_number) # 10**(2) = 100 EXPLICIT
armstrong_numbers = [] #empty list of integers to store armstrong numbers.

for number in range(start_range, end_range):
    sum_of_digits = 0
    temp = number
    while temp > 0:
        digit = temp%10
        sum_of_digits += digit**length_of_number
        temp //= 10
    if number == sum_of_digits:
        armstrong_numbers.append(number)
        break #remove the line from the loop and check all numbers till the end.
else:
    print(f'No Armstrong numbers between {start_range} and {end_range}')
print(f'First Armstrong numbers between {start_range} and {end_range} is {number}')
#print(armstrong_numbers) #to print the list of all
