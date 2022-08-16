'''
This script uses list comprehension to validate a list of passwords based on the below criteria:

Have at least 8 characters or more
Have at least 1 symbol
Have at least 1 lowercase letter
Have at least 1 uppercase letter
Have at least 2 numbers

use of len(password) < 8 to find all the strings that are less than 8 characters (we don't want them so return False others go to the next filter)

use password.isalnum()  to check if all characters in the string are alphanumeric or not. 
it turns True if all characters in the string are alphanumeric (We wanted the strings with at least one Symbol so return False go to the next filter)

use isalpha() if to check if all characters in the string are alphabetic or not. 
It turns True if all characters in the string are alphabetic. 
To test the truth of each element we use any() to loop through the iterable to evaluate the truthiness.
(We wanted the strings with symbols and alphanumeric so return False go to the next filter)

use if password.islower(): to get the strings with least one character is uppercase letter.
The islower() method returns True if all the characters are in lower case, otherwise False.
(We dont know the password to be all the characters are in lower case, so return False go to the next filter)

use if password.isupper(): to get the strings with at least one character is a lowercase letter
The isupper() method returns True if all the characters are in upper case, otherwise False.
(We dont know the password to be all the characters are in upper case, so return False go to the next filter)
    
use if (sum(c.isdigit() for c in password) < 2): to check if the strings/password has at least 2 number characters. 
If the password passes all the above criteria, the function returns True.

'''
def check_password(password):

    #Have at least 8 characters or more
    if len(password) < 8:
        return False
    #Have at least 1 symbol
    if password.isalnum():
        return False
    #Have symbols and alphanumeric
    if not any(c.isalpha() for c in password):
        return False
    #Have at least 1 lowercase letter
    if password.islower():
        return False
    #Have at least 1 uppercase letter
    if password.isupper():
        return False
    #Have at least 2 numbers
    if (sum(c.isdigit() for c in password) < 2):
        return False

    return True

andrews_passwords = ["123456", "hAhA123!", "MyCarR0cks*", "EasyPassword123$$", "AnotherPassword??", "letmein"]
print([password for password in andrews_passwords if check_password(password)])
