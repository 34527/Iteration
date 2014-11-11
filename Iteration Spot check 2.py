#Euan McElhoney
#11/11/2014
#Iteration SC 2

integer = int(input("Please enter an integer: "))
counter = 0

print("Times Table for {0}".format(integer))

for count in range(12):
    counter = counter + 1
    answer = counter * integer

    print(" {0:2} * {1:2} = {2:3}".format(counter, integer, answer))
