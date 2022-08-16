'''
Solve Week 2 exercises using while loops instead of for loops
'''
#1
x = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]

total_lists = len(x)
nested_list_number = 0
while nested_list_number < total_lists:
    items = 0
    while items < len(x[nested_list_number]):
        print(x[nested_list_number][items])

        items += 1
    nested_list_number += 1

#2
range_max = 6
range_min = 1

while range_min<range_max+1:
    number = 1
    while number <= range_min:
        print(range_max, end="")
        number += 1
    range_min += 1
    print(" ")

#3
rangeMin = 4
rangeMax = 1
while rangeMax <= rangeMin:
    
    number1 = 0
    while number1 < rangeMin - rangeMax:
        print("*",end=' ')
        number1 += 1
        
    number2 = 0
    while number2 < rangeMax:
        print(rangeMax, end=' ')
        number2 += 1
    rangeMax += 1
    print()

#4
list1 = [4, 8, 2, 12, 7, 10]
item = 0

while(item < len(list1)):

    if list1[item] % 2 != 0:
        print("List has an odd number")
        break
    item += 1
else:
    print("List does not have an odd number")
        