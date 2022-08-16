'''
Print all individual items stored in the nested list 'nested_list' by using a Nested For loop.
'''
nested_list = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]
for list in nested_list:
    for item in list:
        print(item)
