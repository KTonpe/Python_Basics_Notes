from datetime import date


class Person():
    msg = 'Hi iam a person and here are my info' # class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person_info(self):  # instance variable
        print(f"Name: {self.name} and Age: {self.age}",end =' ')

class Student(Person):   #child class
    def __init__(self, name, age, stud_id,grade):
        super().__init__(name, age) #using super calling parent class constructor
        self.stud_id = stud_id
        self.grade = grade
    def display_student_info(self):
        print(super().msg) # using super caliing class variable
        super().display_person_info() #using super calling parent instance method
        print(f"Student ID: {self.stud_id}, Grade: {self.grade}")

# -------------------------------------------------------------------------------------------------------

class Operations():
    
    def add(self,*nums):
        self.nums = nums
        return sum(self.nums)

# -------------------------------------------------------------------------------------------------------

class Book():
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages + others.pages
    
# -------------------------------------------------------------------------------------------------------
class Salary_formula():
    def __init__(self,salary):
        self.salary = salary
    def __mul__(self,others):
        return self.salary * others.days

class Employee():
    def __init__(self,days):
        self.days = days

# -------------------------------------------------------------------------------------------------------

class Person_age():
    def __init__(self,Dob):
        self.Dob = Dob
        self.Dob_list = self.Dob.split("-")
        self.birth_year = self.Dob_list[0]
    def cal_age_now(self):
        today = date.today()
        return today.year - int(self.birth_year)

# -------------------------------------------------------------------------------------------------------

class BANK:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number in self.accounts:
            print(f"Account with number {account_number} already exists.")
        else:
            self.accounts[account_number] = 0
            print(f"Account with number {account_number} created.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} to account {account_number}. New balance: {self.accounts[account_number]}")
        else:
            print(f"Account with number {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]}")
            else:
                print(f"Insufficient funds in account {account_number}. Current balance: {self.accounts[account_number]}")
        else:
            print(f"Account with number {account_number} does not exist.")

    def show_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance for account {account_number}: {self.accounts[account_number]}")
        else:
            print(f"Account with number {account_number} does not exist.")

# -------------------------------------------------------------------------------------------------------

class ShoppingCart:
    def __init__(self):
        # Initialize an empty dictionary to store items
        self.cart = {}

    def add_item(self, item_name, price):
        # Add the item and its price to the cart
        self.cart[item_name] = price
        print(f"Added {item_name} to the cart with price {price}.")

    def remove_item(self, item_name):
        # Remove the item from the cart if it exists
        if item_name in self.cart:
            del self.cart[item_name]
            print(f"Removed {item_name} from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def display_cart(self):
        self.total = 0
        # Display all items in the cart
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for item_name, price in self.cart.items():
                self.total += price
                print(f"{item_name.title()}: {price:.2f}{chr(0x20B9)}")
            print(f"Total: {self.total:.2f}{chr(0x20B9)}")
# -------------------------------------------------------------------------------------------------------

def student_info():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    stud_id = int(input('Enter your student id: '))
    grade = input('Enter your grade: ')
    sobj = Student(name=name,age =age,stud_id=stud_id,grade=grade)
    sobj.display_student_info()

def Add_Overloading():
    obj = Operations()
    print(obj.add(1,2,3,4,5))
    print(obj.add(1,2,5))

def Adding_Pages_of_two_books():
    b1 = Book(100)
    b2 = Book(200)
    print(b1+b2)

def Calculate_salaray():
    salary = int(input('Enter your salary: '))
    days = int(input('Enter your working days: '))
    sobj = Salary_formula(salary)
    eobj = Employee(days)
    print(f'Total salary received :  {sobj*eobj}{chr(0x20B9)}')

def calculate_age():
    dob = input('Enter your date of birth [YY::MM::DD]: ')
    pobj = Person_age(dob)
    print(f'Your age now is {pobj.cal_age_now()}')

def Banking():
    bank = BANK()
    while True:
        print("""
                1. Create Account
                2. Deposit
                3. Withdraw
                4. Show Balance
                5. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == '1':
            account_number = input("Enter account number: ")
            bank.create_account(account_number)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = int(input("Enter amount: "))
            bank.deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = int(input("Enter amount: "))
            bank.withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.show_balance(account_number)
        elif choice == '5':
            break
        else : print("Invalid choice")

def Add_to_cart():
    cart = ShoppingCart()
    while True:
        print("""
                   1. Add Item
                   2. Remove Item
                   3. Display Cart
                   4. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ").lower()
            price = float(input("Enter price: "))
            cart.add_item(item_name, price)
        elif choice == '2':
            item_name = input("Enter item name: ").lower()
            cart.remove_item(item_name)
        elif choice == '3':
            cart.display_cart()
        elif choice == '4':
            break
        else : print("Invalid input")
# -------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    menu ={
        '1': student_info,
        '2': Add_Overloading,
        '3': Adding_Pages_of_two_books,
        '4': Calculate_salaray,
        '5': calculate_age,
        '6': Banking,
        '7': Add_to_cart,
        'e': exit
        }
    while True:
        print("""
                    1. Student Information
                    2. Add Overloading
                    3. Adding Pages of two books
                    4. Calculate Salary
                    5. calculate age
                    6. Banking
                    7. Add to cart
                    e. exit
              """)
        choice = input("Enter your choice: ")
        menu[choice]() if choice in menu else print("Invalid choice")

