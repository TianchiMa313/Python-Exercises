'''
This script takes a number 'n', 
print i^2 for all non-negative numbers less than n, where i <= n. 
This has the exception for i = 4 and will not print anything.
'''
n = 5
for i in range(0, n+1):
    if i == 4:
        continue
    print(i*i)
