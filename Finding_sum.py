# from_number = int( input('Enter a numnber from : '))

temp=till_number = int(input('Enter a number to find sum untill : '))
sum = 0
while temp > 0:
    sum += temp
    temp -= 1

print(f'{sum} is the addition of natural numbers untill {till_number}')

# for numbers in range(from_number,till_number):
# while from_number > till_number:
#   sum +=from_number
#   from_number +=1
# print(f'sum between{from_number} and {till_number} is {sum}')