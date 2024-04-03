#print multiple lines of the specified format
poem = '''Whose lobster is that? I think I know.
Its owner is quite happy though.
Full of joy like a vivid rainbow,
I watch her laugh. I cry hello.
'''
print('here is a poem for you : ')
print(poem)

print('Here are my details: ')
print('Hello There' , end = ' ')                     # ' , '  is a Seperator
print('Iam a Python Programmer')
print('My name is','Kaustubh', sep =': ')            # sep = ': '  is used to give seperation between different arguments
print('And my age is',22 , sep = ': ')

year = 2024
work_place = 'BlueYonder'
position = 'Apperentice'

# output format 1
print('Current year is : ', year, ' , I work in : ', work_place, ' and My position is : ', position)

#concatination
print('I live in ' + 'Hyderabad.') 

#output Formatting 2
x,y = 1,2
print('\nThe value stored in X is {} and Y is {}'.format(x,y)) 

#user input and data type specifying
z = int(input(('Enter a number which would store in z : ')))
print('The number stored in z is : {} , the type is : {}'.format(z,type(z)))

# facts of print() -> print(OBJECT SEPERATOR END FILE FLUSH)
# by using end = ' ' ; it prints  the text before that
# Default value of file = sys.stdout(screen)
# flush = boolean, specifying if o/p is flushed/buffered ;  Default = False
# type(object) will  give you the datatype of object