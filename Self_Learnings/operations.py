'''
Comparison Operator: ==,!=,>,<,>=,<= -> retuen Boolean (True/Flase)
Logical operator : and,or,not  -> retuen Boolean (True/Flase)
Bitwise Operator : & - (and) , | - (or) , ~ - (not) , ^ - (XOR) , >> - (Bitwise Right shift) , << - (Bitwise Left shift)
Identify  Operator : is , is not -> Boolean
Membership Operator : in , not in -> find the obj in sequence(List,Tuple,Set,Dict) or not 

PRECEDENCE Descending order : () , ** , [+x, -x, ~x]Unary , * , / , // , % , + , - , <<, >> , & , | , ~ , Comp,Iden,Mem , [not,and,or]Logical
'''



num1  =  float(input('Enter the number'))
num2  =  float(input('Enter the number'))
# print(f'The sum of the numbers is {num1+num2}')

#print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))


print(f'Sum is : {num1+num2}')
# alt : num1 += num2 :  print(num1)
print(f'Divisor is : {num1/num2}')          #Normal Division
# alt : num1 /= num2 :  print(num1)
print(f'Floor Divisor is : {num1//num2}') #Floor division = return int because it divides without remainder.
print(f'Remainder is : {num1%num2}')        #Modulus=return the remainder after division
# alt : num1 %= num2 :  print(num1)
print(f'Power of {num1} raise to {num2} is : {num1**num2}') # Power = 2^(3) *Right to Left Associativity*
# alt : num1 **= num2 :  print(num1)

print(num1 < num2)                         #Return Boolean True/False
