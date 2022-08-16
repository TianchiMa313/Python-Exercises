'''
Create key and val and use .items()to find the keys and values in the car_and_price list.
Use if val <= 5000 to print the values that are smaller and equal to 5000.
Use square brackets to print the keys as a list.
'''
car_and_price = {"Ford Mustang": 6590,
                 "Suzuki Swift": 2400,
                 "Jeep Wrangler": 30099,
                 "Honda Civic": 4500,
                 "Toyota Corolla": 4999,
                 "Audi A4": 20000}
print([key for key, val in car_and_price.items() if val <= 5000])
