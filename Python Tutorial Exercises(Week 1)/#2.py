'''
    This script converts all lowercase to uppercase 
    and converts all uppercase to lowercase. 
    Create a string container called "ss".
    If i in s, converts i from lowercase to uppercase 
    and also converts the uppercase to lowercase. 
    x equal converted strings. 
    Add the x to the string container "ss" then print "ss".
'''
s = "Tianchi!@&%#Ma"
ss = ""

for i in s:
    if i.islower():
        x = i.upper()
    elif i.isupper():
        x = i.lower()
    else:
        x = i
    ss += x

print(ss)
