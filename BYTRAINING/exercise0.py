from itertools import zip_longest
from collections import Counter
import sympy

def rev_even_odd_sort_on_string():
    input_string = input('Enter a string : ')
    print(f"""
            Given string is : {input_string}
            String after reversing is : {input_string[::-1]}
            Strings at even positions is : {input_string[::2]}
            String at odd positions is : {input_string[1::2]}
            String after sorting elements is : {sorted(input_string)}
            String in uppercase is :{input_string.upper()}
        """)

def display_alternate_elements():
    input_string1 = input('Enter a string 1: ')
    input_string2 = input('Enter a string 2: ')
    zipped = list(zip_longest(input_string1, input_string2, fillvalue=''))
    flattened = ''.join([x + y for x, y in zipped])
    print(f'String after Alternating elements is : {flattened}')

def fetch_duplicates_and_remove_from_string():
    input_string = input('Enter a string : ')
    lower_case_of_input_string = input_string.lower()
    print(f'Number of occurnace of letters : {Counter(lower_case_of_input_string)}')
    print(f'String after removing duplicates is : {"".join(set(input_string))}')

def count_vowels_in_string():
    input_string = input('Enter a string : ')
    count = sum(1 for i in input_string if i in 'aeiouAEIOU')
    print(f'Number of vowels in given string is : {count}')
    print(f'Number of consonnets in given string is : {len(input_string) - count}')

def multiplication_tabel_of_number():
    number = int(input('Enter a number : '))
    for i in range(1, 11):
        print(f'{number} * {i} = {number * i}')

def display_twin_prime_between_range():
    lower_limit = int(input('Enter lower limit : '))
    upper_limit = int(input('Enter upper limit : '))
    count = []
    if lower_limit != 1 and lower_limit > 1:
        for i in range(lower_limit, upper_limit+1):
            for j in range(i+1, upper_limit+1):
                if (sympy.isprime(i) and sympy.isprime(j)) and (i+j == upper_limit):
                    count.append((i,j))
                    break
        print(f'there are {len(count)} numebrs between 1 and 1000 they are : {count}')
    else : print(f'Invalid Lower limit {lower_limit}')

def find_prime_factors_of_number():
    number = int(input('Enter a number : '))
    print(f'Prime factors of {number} are : {list(sympy.factorint(number))}')

def convert_decimal_to_binary():
    number = int(input('Enter a number : '))
    print(f'Binary of {number} is : {bin(number)}')

if __name__ == '__main__':
    menu = {
        '1': rev_even_odd_sort_on_string,
        '2': display_alternate_elements,
        '3': fetch_duplicates_and_remove_from_string,
        '4': count_vowels_in_string,
        '5': multiplication_tabel_of_number,
        '6': display_twin_prime_between_range,
        '7': find_prime_factors_of_number,
        '8': convert_decimal_to_binary,
        'e': exit
    }
    while True:
        print('''
                1. Reversing a string
                2. Display alternate elements
                3. Fetch duplicates and remove from string
                4. Count vowels in string
                5. Multiplication table of number
                6. Display twin prime between range
                7. Find prime factors of number
                8. Convert decimal to binary
                e. Exit
              ''')
        choice = input('Enter your choice : ')
        menu[choice]() if choice in menu else print('Invalid Choice')