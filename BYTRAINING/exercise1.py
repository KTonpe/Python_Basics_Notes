"""
1. Write a program that asks the user for his name and then welcomes him. The output should look like this:

Enter your name: Saksham
Hello Saksham

2. Write a program that prompts the user to enter two integers and display their sum on the screen.
3. Write a program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit. The formula to convert the temperature is: F = 9/5 C + 32 where F is the Fahrenheit temperature and C is the Celsius temperature. 
4. Write a program which accept principle, rate and time from user and print the simple interest. 
The formula to calculate simple interest is: simple interest = principle x rate x time / 100 
5. Write a program that accepts seconds from keyboard as integer. Your program should converts seconds in hours, minutes and seconds. Your output should like this :

Enter seconds: 13400
Hours: 3
Minutes: 43
Seconds: 20  

6. Write a program that prompts the user to enter number in two variables and swap the contents of the variables. 
7. Write a program that prompts the user to enter number in two variables and swap the contents of the variables.(Do not declare extra variable.)
"""

def hi_statement():
    name = input("Enter your name: ")
    print(f"Hello {name}")

def sum_statement():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum of {num1} and {num2} is {num1+num2}")

def celsius_to_fahrenheit():
    celsius = int(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in fahrenheit is {fahrenheit}")

def simple_interest():
    principle = int(input("Enter principle: "))
    rate = int(input("Enter rate: "))
    time = int(input("Enter time: "))
    simple_interest = (principle * rate * time) / 100
    print(f"Simple interest is {simple_interest}")

def seconds_to_hours_minutes_seconds():
    seconds = int(input("Enter seconds: "))
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")

def swap_statement():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num1, num2 = num2, num1
    print(f"First number is {num1}")
    print(f"Second number is {num2}")

if __name__ == '__main__':
    menu ={
        '1': hi_statement,
        '2': sum_statement,
        '3': celsius_to_fahrenheit,
        '4': simple_interest,
        '5': seconds_to_hours_minutes_seconds,
        '6': swap_statement,
        '7': swap_statement,
        'e': exit
    }
    while True:
        print("""
                1. Ask user name, greet them (e.g., Hello Saksham).
                2. Ask for two numbers, display their sum.
                3. Convert Celsius to Fahrenheit (F = 9/5C + 32).
                4. Get principle, rate, time - calculate simple interest (SI = PRT/100).
                5. Convert seconds to hours, minutes, seconds (output formatted).
                6. Swap values of two user-entered variables.
                7. Swap two variables without using another variable (tricky!).
                e. Exit
              """)
        choice = input("Enter your choice: ")
        menu[choice]() if choice in menu else print('Invalid Choice') 