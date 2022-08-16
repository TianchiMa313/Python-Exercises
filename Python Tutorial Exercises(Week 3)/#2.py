'''
This script prints a list of all prime numbers found between a given range of x and y inclusively. 
This script includes a while loop and a for loop.
The outer loop tells us all the numbers in the given range and 
the inner loop helps us find all prime numbers.
Create a new list 'prime_number_list' to store the values we find from the inner loop.
'''
x = 20
y = 47
prime_number_list = []

# For loop
for i in range(x,y+1):
    for a in range(2,i):
        if i%a == 0:
            break
    else:
        prime_number_list.append(i)
print(prime_number_list)

# While loop
Min = 20
Max = 47
num = Min
prime_numbers = []
# Find all the element between Min and Max
while num >= Min and num <= Max:
    # Notice how we start dividing by 2. This is because (any number)/0 is invalid and any number can be divided by 1.
    # So we will make a variable with the starting value of 2.
    checking_number = 2
    # Check for factors
    while checking_number <= num//2:
        #If i % checking_number is 0 then a break statement moves the control out of the loop and checking_number += 1
        if num % checking_number == 0:
            break
        checking_number += 1
    else:
        #Add the number i to the new prime_numbers list
        prime_numbers.append(num)
    num += 1
print(prime_numbers)
