'''
Prime number is not equals to 1 and less than 1
To find Prime : Divide the number from 2 to given number
if any number from the range dividies then 
assign the flag as True and break the loop and print The number is not Prime
'''


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
