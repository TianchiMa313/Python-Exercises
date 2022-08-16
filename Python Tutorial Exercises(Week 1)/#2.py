'''
This script converts all lowercase to uppercase 
and converts all uppercase to lowercase. 
Create a string container called "new_name".

Create a for loop to check every letter in the 'name' string, 
if it is a lowercase letter convert it to an uppercase letter, 
if it is an uppercase letter convert it to a lowercase letter. 
Check if there are any other elements such as numbers or symbols, 
convert other elements to a space. 
'''
name = "Tianchi!@&%354#Ma"
new_name = ""

for i in name:
    if i.islower():
        x = i.upper()
    elif i.isupper():
        x = i.lower()
    else:
        x = ' '
    new_name += x

print(' '.join(''.join(new_name).split()))
