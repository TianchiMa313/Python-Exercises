'''
    This script will use a for loop to find the common elements 
    in the 'shopping_list' and 'store_products', 
    it prints the fist common element only by using the break statement.
'''
store_products = ["fruit", "water", "bread", "toilet paper", "soap"]
shopping_list = ["eggs", "tooth paste", "toilet paper", "ice cream", "water"]

for x in shopping_list:
    if x in store_products:
        print(x)
        break
    