'''
This script uses both while loop and for loop to unwrap any nested list into a single list.
This script accepts a nested list as an argument, and then iterates over each element in that list. 
For each element, it checks if its type is a list or not by using the function isinstance().
If yes, then again calls the same function nest_list() with this element (list) to get a flat list out of it. 
Then extends the main flat list with the returned flat list.
Whereas, if the element is not a list then it adds that to the end of the list using flat_list.append().
'''
nested_list = ["this", "item", ["is", "a", ["a", "mess"], "needs", "to", ["be", "unwrapped"]], ["into", "a"], "single", ["item"]]
# For loop
def nest_list(nested_list):

    flat_list = []
    # Iterate over all the elements in given list
    for i in nested_list:
        # Check if type of element is list(all the elements)
        if isinstance(i, list):
            # Extend the flat list by adding contents of this element (list)
            flat_list.extend(nest_list(i))
        else:
            # Append/add the elemengt to the list
            flat_list.append(i)    
    return flat_list

print(nest_list(nested_list))

#While loop
def nest_list2(nested_list):
    
    flat_list2 = []
    num = 0
    
    while num < len(nested_list):
        if isinstance(nested_list[num], list):
            flat_list2.extend(nest_list2(nested_list[num]))
            
        else:
            flat_list2.append(nested_list[num])
    
        num += 1
    return flat_list2

print(nest_list2(nested_list))
