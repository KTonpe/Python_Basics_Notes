'''
Used round( , x) function to round off the float to x decimals 
'''

km = float(input('Enter the kilo meters to convert into Miles : '))
#conversion factor from km to miles
con_from_km_to_miles = 0.621371
miles = km * con_from_km_to_miles
print(f'Conversion of {km}KM is  {round(miles,2)} miles')
