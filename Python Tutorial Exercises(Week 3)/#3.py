'''
This script takes an input number 's' and stores the number to the variable name called 'total_number'. 
and adds a number to the 'week_number' list to count the weeks. When the 'total_number' 
is greater than the goal then print the number of weeks that have passed and 
the final amount he has saved once the goal has been reached.
'''

g = 1000
week_number = 0
total_number = 0

while g > total_number :  

    # Add one to the week_number list/container, every time Andrew enter a number
    week_number += 1
    # Add the input number to the total list/container
    total_number += int(input("Enter a number: "))
# Once the 'total number' is greater then 'g'($1000),print the message
print(f"He has saved enough at week {week_number} with a total of $ {total_number}.")
