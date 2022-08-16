'''
Take a list of names and convert it to a dictionary with the key being the name 
and the value is the length of the name.
Remove any name that has 7 characters or more.
Use dictionary comprehension to find the name that is less than 7 characters, 
if len(i) < 7 add them to the dictionary called name_dictionary.
print name_dictionary at the end.
'''

names = ["Raphael", "Tanya", "Miriam", "Leonard", "Owen", "Julie", "Haleema", "Mabel", "Stanley"]

name_dictionary = {i : len(i) for i in names if len(i) < 7}
print(name_dictionary)
