'''
FACTS: 
for loop doesnt support float
Log (base=  number) ^ (result) = (power) -> number^power = result
'''



# count = 10
# number = int(input("Enter a number for power Table: "))
# for i in range(count+1):
#     print(f'{number} raised to the power {i} = {number ** i}')


'''#Using map and list
result = list(map(lambda x: 2**x, range(count)))
for i in range(count):
    print(f'2 raised to power {i} is {result[i]}')'''

'''
#Using list to store the tables

power_multiplication =[]
for i in range(count+1):
    power_multiplication.append(number**i)
print(power_multiplication)'''

#my logic: to find the base and power of a number given 
result = int(input('Enter a number to find its number: '))
for i in range(result):
    for j in range(result):
        if i ** j == result:
            print(f'{i} to the power of {j} is {i ** j}')

# result = int(input('Enter a number to find its number: '))
# for exponent in range(2,result**0.5)