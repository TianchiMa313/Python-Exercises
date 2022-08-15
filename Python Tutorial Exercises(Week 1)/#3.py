'''
    Find all overlapping matches
    This script takes a given input string a and substring b, 
    made a 'count' container to store the number of times 
    the substring appears in the string.
    c = len(b) = 2 then use for loop and a[i:i+c] to check every 2 items/character(01,12,23,34...)
    to see if there any b/'ha' in a string.
    It add one a number to 'count' every time it find a b/'ha' in that string, 
    print 'count' value at the end of the for loop.
'''
a = "harry had a little lamb"
b = "ha" 
count = 0
c = len(b)
for i in range(len(a)):
    if a[i:i+c] == b:
        count += 1
print(count)
