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

year =   int(input('Enter the Year in number format: '))
month  = int(input('Month in number format: '))

if year > 0: #here year must be INT 
    result = f'{year} is a leap year' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else f'{year} is not a leap year'
    print(result)
    print(calendar.month(year, month)) if (month > 0 and month < 13) else print(f'give a valid {month}')
else : print(f'Enter a valid year')       


'''if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print(f'{year} is a leap year')
else: print(f'{year} is not a leap year')'''

'''if (year % 400 == 0) and (year % 100 == 0):
    print(f'{year} is a leap year')
elif (year % 4 ==0) and (year % 100 != 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''

