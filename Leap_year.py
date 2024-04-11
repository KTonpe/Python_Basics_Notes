'''
The condition for Leap year are :
1. If the year is evenly divisible by 4, it is a leap year.
2. if the year is evenly divisible by 100, it is not a leap year.
3. but, The year is also evenly divisible by 400, it is a leap year.

so point (1,2) -> AND ; point 3 -> OR
'''

#calender module to print month calender
#to print the calender expression -> calender.month(year,month)
import calendar
import unittest

def leap_year(year):
    if year > 0: #here year must be INT 
        year_condition = f'{year} is a leap year' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else f'{year} is not a leap year'
        # if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        #     year_condition = f'{year} is a leap year'
        # else:
        #     year_condition = f'{year} is not a leap year' 

    else : year_condition = f'Enter a positive year number'       
    return year_condition

#unit testing

class Testing_leap_logic(unittest.TestCase):
    def setUp(self):
        self.not_a_leap_year = 2023
        self.negative_year = -2000
        self.hundread_year = 2200
        self.multiple_of_four = 2004
        self.month1 = 4
        self.month2 = 13
    def test_not_multiple_of_four_years(self):
        result = leap_year(self.not_a_leap_year)
        year = self.not_a_leap_year
        month = self.month1
        self.assertEqual(result, f'{self.not_a_leap_year} is not a leap year')
        if (self.not_a_leap_year > 0) : print(calendar.month(year, month)) if (month > 0 and month < 13) else print(f'give a valid month \n')
    def test_negative_years(self):
        result = leap_year(self.negative_year)
        year = self.negative_year
        month = self.month2
        self.assertEqual(result, 'Enter a positive year number')
        if (self.negative_year > 0) : print(calendar.month(year, month)) if (month > 0 and month < 13) else print(f'give a valid {month} \n')
    def test_hunderaded_years(self):
        result = leap_year(self.hundread_year)
        year = self.hundread_year
        month = self.month1
        self.assertEqual(result, f'{self.hundread_year} is not a leap year')
        if (self.hundread_year > 0) : print(calendar.month(year, month)) if (month > 0 and month < 13) else print(f'give a valid {month} \n')
    def test_four_years(self):
        result = leap_year(self.multiple_of_four)
        year = self.multiple_of_four
        month = self.month2
        self.assertEqual(result, f'{self.multiple_of_four} is a leap year')
        if (self.multiple_of_four > 0) : print(calendar.month(year, month)) if (month > 0 and month < 13) else print(f'give a valid {month} \n')

unittest.main()
year =   int(input('Enter the Year in number format: '))
#month  = int(input('Month in number format: '))
print(leap_year(year))

'''if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print(f'{year} is a leap year')
else: print(f'{year} is not a leap year')'''

'''if (year % 400 == 0) and (year % 100 == 0):
    print(f'{year} is a leap year')
elif (year % 4 ==0) and (year % 100 != 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''

