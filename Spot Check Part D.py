#Euan McElhoney
#11/11/2014
#Iteration Spot check - Part D

number = 0
total = 0

while number != -1:
    number = int(input("Please enter a number: "))
    if number != -1:
        total = total + (number * number)

print("The total is {0}".format(total))
