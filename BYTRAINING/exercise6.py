"""
2. Write a Program to create a valid empty class with the name Students, with no properties.
"""
class Empty_class():
    pass
"""
1. Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.
"""
class Student():
    def __init__(self, name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

stud = Student('Kaustubh',6,'B')
stud.display()

"""
3.Write a program to create a child class Teacher(name, age) that will inherit the properties from the parent class Staff(role, dept, salary) and display the staff details using show_details(self)
output:
Name:  Raj
Age:  28
Role: Teacher
Department: Science
"""

class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, age, role, dept, salary):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name:\t{self.name}, Age:\t{self.age}, Role:\t{self.role}, Department:\t{self.dept}")


teacher = Teacher(name='Raj',age=6,role='Teacher',dept='Science',salary=2)
teacher.show_details()

"""
4)Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the busFare() in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.
"""

class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
        self.fare = self.capacity * 100
    def fare_details(self):
        print(f"The total fare is {self.fare:.2f}")  # Format output to 2 decimal places

class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)
    def busFare(self):
        maintenance_charge = self.fare * 0.1
        total_fare = self.fare + maintenance_charge
        print(f"The total Bus fare (including 10% maintenance charge) is {total_fare:.2f}")  # Format output to 2 decimal places


# Create objects for Vehicle and Bus classes
vehicle = Vehicle(10)
bus = Bus()

# Call methods to display fare details
vehicle.fare_details()
bus.busFare()

"""
5-a: New Class Which Inherits

A new class named F14 is initiated for you which inherits from the parent class Jets.

Instead of taking parameters other than self such as name and country, initiate the new class so that name is always fixed to "F14" and origin is always fixed to "USA"

Make sure the new class has its own initiation method (constructor or __init__) which takes only one parameter:self and overrides name and origin attributes as those don't change for an F14 fighter jet.
"""

class Jets:
    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class F14(Jets):
    def __init__(self, name ='F14',origin = 'USA'):
        self.name = name
        self.origin = origin
        super().__init__(self.name, self.origin)

a = F14()
print(a.origin)
print(a.name)