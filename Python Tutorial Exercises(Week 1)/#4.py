'''
This script will use a for loop to find the first common element in both lists.
First common element only, so we can use a break statement to stop the loop after finding the first common element.
'''
store_products = ["fruit", "water", "bread", "toilet paper", "soap"]
shopping_list = ["eggs", "tooth paste", "toilet paper", "ice cream", "water"]

for x in shopping_list:
    if x in store_products:
        print(x)
        break
    