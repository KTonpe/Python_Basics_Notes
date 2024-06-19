"""
1. Write a program that accepts a list from user and print the alternate element of list.

How many elements you want to enter? 6
Enter 6 elements
10
20
30
40
50
60
Alternate elements are:
10
30
50

2. Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.

3. Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard. 

4. Write a program that rotates the element of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.

How many elements you want to enter? 4
Enter 4 elements
sunday
monday
tuesday
wednesday
list before shifting ['sunday', 'monday', 'tuesday', 'wednesday']
list after shifting ['wednesday', 'sunday', 'monday', 'tuesday']

5. Write a program that input a string and ask user to delete a given word from a string.

6. Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the form March 12, 2021.
"""

def display_alternate_elements_from_list():
    input_list_length = int(input('Enter the length of a list : '))
    input_list = []
    for i in range(input_list_length):
        input_list.append(input(f'Enter element at {i+1} index  : '))
    print(f'Given list is : {input_list}')
    print(f'Alternate elements are: {input_list[::2]}')

def reverse_list_content():
    input_list_length = int(input('Enter the length of a list : '))
    input_list = []
    for i in range(input_list_length):
        input_list.append(input(f'Enter element at {i+1} index  : '))
    print(f'Given list is : {input_list}')
    print(f'Reversed list is : {input_list[::-1]}')

def find_largest_number_in_list():
    input_list_length = int(input('Enter the length of a list : '))
    input_list = []
    for i in range(input_list_length):
        input_list.append(int(input(f'Enter element at {i+1} index  : ')))
    print(f'Given list is : {input_list}')
    largest_number = input_list[0]
    for i in input_list:
        if i > largest_number:
            largest_number = i
    print(f'Largest number in list is : {largest_number}')

def rotate_list_elements():
    input_list_length = int(input('Enter the length of a list : '))
    input_list = []
    for i in range(input_list_length):
        input_list.append(input(f'Enter element at {i+1} index  : '))
    print(f'list before shifting {input_list}')
    for i in range(len(input_list)-1):
        input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    print(f'list after shifting {input_list}')

def delete_word_from_string():
    input_string = input('Enter a string : ')
    input_word = input('Enter a word to delete : ')
    print(f'Given string is : {input_string}')
    print(f'Word to delete is : {input_word}')
    input_string = input_string.replace(input_word, '') if input_word in input_string else print(f' "{input_word}" is not found in given string : "{input_string}"')
    print(f'String after deletion is : {input_string}')

def convert_date_format():
    input_date = input('Enter a date in the form mm/dd/yyyy : ')
    print(f'Given date is : {input_date}')
    month, day, year = input_date.split('/')
    month = int(month)
    day = int(day)
    if(1<= month <= 12) and (1<= day <= 31):
        calender_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        month = calender_list[month-1]
        print(f'Date in Month Day, Year format is : {month} {day}, {year}')
    else : print('Input data(Month or Date) is out of range')

if __name__ == '__main__':
    menu = {
        '1':  display_alternate_elements_from_list,
        '2' : reverse_list_content,
        '3' : find_largest_number_in_list,
        '4' : rotate_list_elements,
        '5' : delete_word_from_string,
        '6' : convert_date_format,
        'e' : exit
    }
    while True:
        print("""
                    1. Print Every Other List Element
                    2. Reverse List Content (Manual Approach)
                    3. Find Largest Number in List (Without max())
                    4. Rotate List Elements (Shifting)
                    5. Delete a Word from a String
                    6. Convert Date Format (mm/dd/yyyy to Month Day, Year)
                    e. exit
            """)
        choice = input('Enter your choice: ')
        menu[choice]() if choice in menu else print('Invalid Choice')
            
