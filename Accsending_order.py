limit = int(input("Enter the limit: "))
#print(limit)
list_of_numbers = []
for i in range(0,limit):
    #list_of_numbers.append(int(input("Enter the number: ")))
    num = int(input("Enter the number: "))
    list_of_numbers += [num]
    

list_of_numbers.sort()
print(list_of_numbers)

location = int(input('Enter the location: '))
number = int(input('Enter the number: '))
list_of_num =[0]*(location+1)
list_of_num[location] = number 

print(list_of_num)