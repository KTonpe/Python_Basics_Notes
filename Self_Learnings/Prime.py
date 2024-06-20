'''
Prime number is not equals to 1 and less than 1
To find Prime : Divide the number from 2 to given number
if any number from the range dividies then 
assign the flag as True and break the loop and print The number is not Prime
'''

#Find out if it's a prime number
number = int(input('Enter a number: '))
flag = False
if number == 1: print(f'{number} is not Prime')
elif number > 1:
    for i in range(2, number): #we can change the range from number -> (number // 2)
        if number % i == 0:
            flag = True
            break
    print(f'{number} is not Prime') if flag else print(f'{number} is Prime') #if true -> prime   
else : print(f'{number} is not Prime')

#Prime Numbers between the range
start_number = int(input('Enter start number: '))
end_number = int(input('Enter end number: '))

if start_number != 1 and start_number > 1:
    print(f'Prime numbers between {start_number} and {end_number} are : ')
    for num in range(start_number,end_number):
        count = [] #count = 0
        for factors in range(2,num):
            if num % factors == 0:
                count.append(factors) # count += 1
                break
        if len(count) == 0: print(num) #if count == 0:
else : print('Enter a valid start/end number!')
