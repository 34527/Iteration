#Euan McElhoney
#21/10/14
#Iteration Class exercises - Development 4

text = input("please enter a string: ")
length = len(text)
length = length -1

for index in range(length, -1, -1):
    print(text[index])
