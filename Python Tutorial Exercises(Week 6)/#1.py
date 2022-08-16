'''
Andrew wishes to create a python class Car to help him with organising data he has on the cars he loves.
Example input:
new_car = Car("SSC", "Tuatara", 2020, 283, 2000000, 50677)

Organising data by using class and methods.
Created an __init__ method to store all the elements we need
Created 3 methods as asked: print_name, print_info and estimate_value. 
print_name: print the make and model. Use self.make & self.model will be easier to manage for later on.
print_info: print all the information about the car.
estimate_value: returns an estimate.
'''

class Car:
    #Instance variables 
    def __init__ (self, make, model, year, max_speed, purchase_price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.purchase_price = purchase_price
        self.mileage = mileage

    def print_name(self):
        print(self.make,self.model)

    def print_info(self):
        print(f'Mark: {self.make}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Max speed: {self.max_speed}mph')
        print(f'Purchase price: ${self.purchase_price}')
        print(f'Mileage: {self.mileage}km')

    def estimate_value(self):
        return (round(self.purchase_price * (1 - self.mileage / 300000)**(2022-self.year)))

#              Mark     Model   Year   MS   price   Mileage
new_car = Car("SSC", "Tuatara", 2020, 283, 2000000, 50677)

new_car.print_name()
new_car.print_info()
new_value = new_car.estimate_value()
print(new_value)
