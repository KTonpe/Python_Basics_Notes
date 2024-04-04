'''
Used round( , x) function to round off the float to x decimals 
'''

km = float(input('Enter the kilo meters to convert into Miles : '))
#conversion factor from km to miles
con_from_km_to_miles = 0.621371
miles = km * con_from_km_to_miles
print(f'Conversion of {km}KM is  {round(miles,2)} miles')


celsius = float(input('Enter the temperature in Celsius: '))
fahrenheit = (celsius * 1.8) + 32    #conversion from Celsius to Fahrenheit
print(f'The temperature {celsius}\'c in Fahrenheit is {round(fahrenheit,2)}')
fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8   #conversion from Fahrenheit to Celsius
print(f'The temperature {fahrenheit}\'f in Celsius is {round(celsius,2)}')
