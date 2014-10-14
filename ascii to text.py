#Euan McElhoney
#10/10/14
#ASCII Task 1

print("This program will give you the option either convert an ASCII code to a text character or a text character to ASCII")
print("To convert to Text press 1, To convert to ASCII press 2")

option = int(input("Please enter your selection"))

if option == 1:
    ascii_code = int(input("Please enter the code you would like to convert to text"))
    ascii_text = chr(ascii)
    print("The code entered represents the character {0}".format(ascii_code))

