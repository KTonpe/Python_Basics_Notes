"""
1)Write a program that reads string from user. Your program should create a dictionary having key as word length and value is count of words of that length. For example, if user enters 'A fat cat is on the mat'.

Word	Word length
A	1
fat	3
cat	3
is	2
on	2
the	3
mat	3
The content of dictionary should be {1:1, 3:4, 2:2}

2)Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD. Dictionary's value should be stored in list. Your dictionary should be like:
{'EVEN':[8,10,64], 'ODD':[1,5,9]}
"""

def word_length_count():
    string = input("Enter a string: ")
    word_length_dict = {}
    for word in string.split():
        if len(word) in word_length_dict:
            word_length_dict[len(word)] += 1
        else:
            word_length_dict[len(word)] = 1
    print(word_length_dict)

def Even_Odd_Number_Dictionary():
    even = []
    odd = []
    for i in range(6):
        number = int(input("Enter a number: "))
        even.append(number) if number % 2 == 0 else odd.append(number)

    even_odd_dict = {'EVEN': even, 'ODD': odd}
    print(even_odd_dict)

if __name__ == '__main__':
    menu ={
        '1': word_length_count,
        '2': Even_Odd_Number_Dictionary,
        'e': exit
    }
    while True:
        print("""
                    1. Word length count
                    2. Even and Odd number dictionary
                    e. exit
              """)
        choice = input("Enter your choice: ")
        menu[choice]() if choice in menu else print("Invalid choice")