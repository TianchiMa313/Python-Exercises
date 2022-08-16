'''
Use nested for loop and range to find the different food combinations.
The outer loop tells us the first item we needed and the inner loop tells us the second item we needed. 
If the outer loop and the inner loop have the same value/item skip it by using if i == item: continue.
'''
Ingredient_list = ["rice","cheese", "pasta", "tomato sauce", "broccoli"]
for i in range(0, len(Ingredient_list)):
    for item in range(i, len(Ingredient_list)):
        if i == item:
            continue
        print(Ingredient_list[i], "and", Ingredient_list[item])
