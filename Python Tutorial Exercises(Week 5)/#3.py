'''
Extract all numbers from a string text and print the sum of them using list comprehension.  
Use for loop and .split() to split the string.
Use if s.rstrip(",.") to remove the remove commas and full stops from the string and find all the number that is in the string by using .isdigit().
We get a list of strings:['2018', '1000000', '2019', '5', '2020', '2'].
'2018' is a string in the list, have to convert the string to a number. Use int(i) to convert the strings to numbers.
Use sum() to add all the numbers together. 
Print the total number out.
'''

my_string = "Back in the early 2010s, Andrew has always had a keen interest in cars. So much that in 2018, he spent over 1000000 in cash just to buy his favorite car. In 2019, he sold that car just to buy 5 other cars. However, when covid-19 hit NZ in 2020, he had to sell all but 2 of his cars."

print(sum([int(i) for i in [s.rstrip(",.") for s in my_string.split()] if i.isdigit()]))
