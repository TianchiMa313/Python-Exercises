'''
Check if a given list 'number_list' contains an odd number. 
Iterate each element in the list using for loop and 
check if num % 2 != 0. If the condition satisfies, 
print "List has an odd number", 
else print "List does not have an odd number".
'''
number_list = [4, 8, 2, 12, 7, 10]

for num in number_list:

    if num %2 != 0:
      print("List has an odd number")
      break
else:
    print("List does not have an odd number")
