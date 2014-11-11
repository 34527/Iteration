#Euan McElhoney
#11/11/2014
#Iteration Spot Check 3

import random

guessed = False
number = random.randint(1,100)
noOfTurns = 0

while guessed is False:
    noOfTurns = noOfTurns + 1
    userguess = int(input("Enter your guess for the number: "))
    if userguess == number:
        guessed = True
    elif userguess > number:
        print("The number you guessed is too high")
    else:
        print("the number you guessed was too low")
print("You took {0} turns to guess the number".format(noOfTurns))
print("The number was {0}".format(number))

    
