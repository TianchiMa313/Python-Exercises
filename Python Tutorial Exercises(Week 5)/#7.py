'''
This script uses dictionary comprehension to help Andrew to track the car prices. 
Help him consolidate the car to its current price using dictionary comprehension, 
by adding the value from the old price, January increase and February increase together. 

Use a for loop :for i in range(len(cars)) to get the order of the cars. 
The length of every list is the same so we can use 'i' to help us match car names with 3 price lists 
and use the "+" to add the value from the old price, January increase and February increase together. 
Print the current price at the end.
'''

cars = ["Hyundai Kona", "Kia Soul", "Mazda CX-30", "Volkswagen Taos", "BMW X1", "BMW X2"]
old_prices = [22545, 20505, 23425, 24490, 36395, 37595]
jan_increase = [540, 120, 600, 199, 1000, 3050]
feb_increase = [153, 200, 123, 385, 450, 600]

print({cars[i]: old_prices[i]+jan_increase[i]+feb_increase[i] for i in range(len(cars))})
