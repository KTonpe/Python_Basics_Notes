class FormulaError(Exception):
    def __init__(self, message):
        self.message = message

def open_file(filename):
    try:
        with open(filename, 'r') as f:
            return f
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None  # Indicate file not found

def read_from_file():
    file = open_file("non-existent-file.txt")  # Example usage with potential error
    if file:
        contents = file.read()
        print(contents)
    else:
        print("File not opened.")

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_num_values():

    num1 = get_numeric_input("Enter the first number: ")
    num2 = get_numeric_input("Enter the second number: ")

    try:
        print("The numbers you entered are:", num1, num2)
    except (TypeError, ValueError) as e:  # Catch both potential exceptions
        print("Error:", e)  # Generic error message

def get_integer_list():
    user_input = input("Enter a comma-separated list of integers (e.g., 1, 2, 3): ")
    try:
        string_list = user_input.split(",")
        integer_list = [int(item.strip()) for item in string_list]
        return integer_list
    except ValueError: print("Invalid input. Please enter only comma-separated integers.")
def get_valid_index(list_length):
    while True:
        try:
            index = int(input(f"Enter an index (0 to {list_length - 1}): "))
            if 0 <= index < list_length:
                return index
            else:
                print(f"Index out of range. Please enter a value between 0 and {list_length - 1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
def get_a_list():
    my_list = get_integer_list()
    list_length = len(my_list)
    if list_length > 0:
        try:
            index = get_valid_index(list_length)
            print("The element at index", index, "is", my_list[index])
        except IndexError:
            print("IndexError: list index out of range")
def interactive_calculator():
    while True:
        try:
            expression = input("Enter the expression : ")
            filtered_list= [item.strip() for item in expression]
            elements_from_expression= [item for item in filtered_list if item]
            if len(elements_from_expression) != 3 or elements_from_expression[1] not in ("+", "-", "*", "/"):
                raise FormulaError("Invalid expression format. Please use 'operand operator operand'.")
            num1 = float(elements_from_expression[0])
            num2 = float(elements_from_expression[2])
            operator = elements_from_expression[1]
            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                if num2 == 0:  # Handle division by zero
                    raise FormulaError("Division by zero is not allowed.")
                print(num1 / num2)
            else:
                print("Invalid operator")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except FormulaError as e:
            print(e.message)  # Print the custom error message
        except Exception as e:  # Catch unexpected errors
            print(f"An unexpected error occurred: {e}")

def Grade_calculator():
    try:
        grades_in_string = input("Enter the grades seperated by commas : ").strip().split(',')
        grades = [float(item) for item in grades_in_string if item]
        average_grade = sum(grades) / len(grades)
        print(f"The average grade is: {average_grade:.2f}")
    except ValueError:
        print("Invalid input. Please enter only integers using comma-separated.")
if __name__ == '__main__':
    menu = {
        '1': read_from_file,
        '2': get_num_values,
        '3': get_a_list,
        '4': interactive_calculator,
        '5': Grade_calculator,
        'e': exit
    }

    while True:
        print("""
                1. Read from file
                2. Get numeric input
                3. Get a list
                4. Interactive calculator
                5. Grade calculator
                e. Exit
        """)
        choice = input("Enter your choice: ")

        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice")
