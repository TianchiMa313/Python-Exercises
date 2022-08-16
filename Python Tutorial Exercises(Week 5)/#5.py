'''
Use dictionary comprehension to swap the key values in a dictionary.
Use key and val and .items() to find the keys and the values in the dictionary first.
Create a new dictionary then place the value first then the key second then.
Print the new dictionary at the end.
'''
dictionary_x = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}

print({val: key for key, val in dictionary_x.items()})
