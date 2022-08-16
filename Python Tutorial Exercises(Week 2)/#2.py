'''
The outer loop iterates through the range from 0 to 6 and for each number/item in that sequence.
It enters the inner loop where it iterates over a range of that item.
The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.
For each iteration of the outer loop, the columns count gets incremented by 1
In each iteration of an inner loop, we print 'number' which is 6.
'''
number = 6
for i in range(0, number):
    for w in range(0, i+1):
        print(number, end="")
    print("\r")
