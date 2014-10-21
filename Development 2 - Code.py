#Euan McElhoney
#21/10/14
#Iteration Class exercises - Development 4

column = int(input("Please enter how many columns you want: "))
row = int(input("Please enter how many rows you want: "))
table = ""
for count in range(column):
    table = table + "*"
for count in range(row):
    print(table)

