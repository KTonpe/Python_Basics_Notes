# from_number = int( input('Enter a numnber from : '))
import unittest


def my_function(temp):
    if temp > 0:
        sum = 0
        while temp > 0:
            sum += temp
            temp -= 1
    else: sum = None
    return sum


class Sum_testings(unittest.TestCase):
    def setUp(self): #note the Upper and Lower-case  of "setUp"
        self.a = 2
        self.b = 4
    def test_positive_number1(self):
        print(f'Test 1 called')
        result = my_function(self.a)
        self.assertEqual(result, 3)
    def test_positive_number2(self):
        print(f'Test 2 called')
        result = my_function(self.b)
        self.assertEqual(result, 10)

unittest.main()
temp=till_number = int(input('Enter a number to find sum untill : '))
print(f'{my_function(till_number)} is the addition of natural numbers untill {till_number}')

# for numbers in range(from_number,till_number):
# while from_number > till_number:
#   sum +=from_number
#   from_number +=1
# print(f'sum between{from_number} and {till_number} is {sum}')