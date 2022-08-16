'''
This script takes in an argument n and prints the factorial output, 
without using any math libraries. A factorial of a number is represented by n!, 
for example, 3! = 3 x 2 x 1 = 6. 
This script includes a while loop and a for loop.
'''
num = 5
factorial = 1
# For loop
for i in range(1, num+1):
    factorial=factorial*i
print(factorial)

# While loop
factorial2 = 1
while num > 0:
    factorial2 = factorial2 * num
    num = num - 1
print(factorial2)
