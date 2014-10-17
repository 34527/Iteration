#Euan McElhoney
#17/10/14
#iteration - revision 4


valid = False

while not valid:
    number = int(input("Please enter a number between 10 and 20: "))
    if number>=10 and number<=20:
        valid = True
    else:
        print("Number invalid, please try again")

print("Number valid")
        
