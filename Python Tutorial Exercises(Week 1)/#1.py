'''
    This script takes a number n, prints i^2 for all non-negative numbers 
    that are less than n, where i <= n. 
    This has the exception for i = 4 and will not print anything. 
'''
n = 5
for v in range(0, n+1):
    if v == 4:
        continue
    print(v*v)
