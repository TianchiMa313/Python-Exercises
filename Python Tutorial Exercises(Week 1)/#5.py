'''
    The script will find the first number divisible by 7 
    in the range of two given input numbers x and y. 
'''
x = 8
y = 30
for i in range(x,y):
    #find the numbers which are divisible by 7.
    if i%7 == 0:
        print(i)
        break
