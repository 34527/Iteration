#Euan McElhoney
#17/10/14
#Iteration - Revision 5

total_sum = 0
input_number = 0
total_number = 0


while input_number >=0:
    input_number = int(input("Please enter a number: "))
    if input_number >=0:
        total_sum = total_sum + input_number
        total_number = total_number + 1

average = total_sum / total_number

print("The average is {0}".format(average))
