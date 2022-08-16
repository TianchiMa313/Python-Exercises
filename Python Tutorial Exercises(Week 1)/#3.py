'''
Find all overlapping matches
This script takes a given input string 'first_string' and 'second_string'.
A 'count' container to store the number of times.
Print the number of times the substring appears in the string.

check = len(b) = 2 then use for loop and a[i:i+check] to check every 2 items/character(01,12,23,34...)
to see if there are any 'ha' in string 'first_string'.
It adds one to 'count' every time it finds a 'ha' in 'first_string', 
prints the' count' value at the end of the for a loop to show how many 'ha' in 'first_string'.
'''
first_string = "harry had a little lamb"
second_string = "ha" 
count = 0
check = len(second_string)
for i in range(len(first_string)):
    if first_string[i:i+check] == second_string:
        count += 1
print(count)
