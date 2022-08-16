'''
This script uses for loop to find the youngest and oldest employees. 
Find the youngest and oldest employees by comparing and updating new values using a for loop and an if statement.
'''
company = {"john": 99, "ben": 34, "kevin": 45, "janet": 20, "jack": 50, "jean": 87}

minimum = list(company.values())[0]
youngest_name = None 

for y_name in company:
    if company[y_name] < minimum:
        minimum = company[y_name]
        youngest_name = y_name
print(f"Youngest employee award goes to {youngest_name} at age {minimum}.")

maximum = 0
oldest_name = None
for o_name in company:
    if company[o_name] > maximum:
        maximum = company[o_name] 
        oldest_name = o_name
print(f"Oldest employee award goes to {oldest_name} at age {maximum}.")
