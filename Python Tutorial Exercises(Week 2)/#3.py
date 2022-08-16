'''
This script takes a given input number x, using the reverse for loop and a nested for loop 
to print the Downward half-Pyramid Pattern of star and a Upward half-Pyramid Pattern of number together. 

The outer loop tells us the number of rows, and the inner loop tells us 
the column needed to print the pattern.

Downward half-Pyramid Pattern of star
Where numbers get reduced in each iteration, and on the last row. 
We use stars to replace the numbers here. 

Upward half-Pyramid Pattern of number
In this number pattern, we display a single digit on the first row, 
the next two digits of the second row, And the following three numbers 
on the third row and this process will repeat till the number of rows is reached.
'''
bow_column = 4
# Outer loop
for i in range(1, bow_column+1):
    # Nested loop
    for j in range(bow_column, 0, -1):
        num = i
        if j > i:
            # Display star
            print("*", end=' ')
        else:
            # Display number
            print(num, end=' ')
            num += 1
    # New line after each row
    print()
    