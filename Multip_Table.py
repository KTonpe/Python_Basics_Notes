number = int(input('Enter a number to print it\'s table: '))
limit = int(input('Enter the Limit number : '))

# using step index in for loop
for i in range(0,(number*(limit+1)),number):
    print(i)