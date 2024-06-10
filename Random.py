import random

names = ['Kaustubh','Chintu','Ram',"Ganesh",'Krishna']

print(random.randint(1,4)) #Returns a random integer between a and b inclusive
print(random.uniform(1,5)) #return random float between 1,5
print(random.randrange(0,50,5)) #technically return random multiple of 5 in the range of 1 to 50
print(random.random()) #Return the next random floating point number in the range [0.0, 1.0)

print( f'\nList is {names} \n')
print(random.choice(names)) #Return a random element from the non-empty sequence
print(random.sample(names,2)) #Returns k length list of unique elements from the sequence
random.shuffle(names) #Non Return type and Shuffles the list *can be used for cards
