'''
Andrew has stored the car data in various formats, 
help him consolidate them all into a list of the new variable of cars, 
he only cares about the cars from the cars_i_bought list. 
You should name this new list andrews_cars.

This script helps Andrew to find out the car data about the cars he bought. 
Which include: make, model, year, max speed, purchase price, and mileage.

The length and the data place and order of each list are the same 
so we can use the cars_i_bought list and a for loop to match the data of the cars.
'item' (a temporary variable) = the car names in the 'cars_i_bought' list 
and also equals the location of the car name in the list.

####Makes#####
We can retrieve the car model from the makes dictionary to get the car mark. 
Create 2 variables 'makes_model and makes_brand' and .items() to get the keys and values in 'makes' dictionary. 
Use 'if car_name == makes_model' to do name comparison. 
If the name is the same,  'car_marks = makes_brand' use '=' to assignment makes_brand a new name called car_marks.
Place 'car_marks' in the right order in car_check.

####speeds#####
for car_speeds we can combine the 'year' and the 'cars_i_bought' list together, 
to retrieve the speeds dictionary. The process is the same as the one above.
Place 'car_speeds' in the right order in car_check.

Place those variables in the same order as 'def __init__' in class Car in 'car_check' 
then append 'car_check' to the list of andrews_cars.
'''

class Car:
   
    def __init__(self, make, model, year, max_speed, purchase_price, mileage):
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


makes = {"Veyron Super Sport": "Bugatti",
         "Venom GT": "Hennessey",
         "A8": "Audi",
         "ES": "Lexus",
         "Senna": "McLaren",
         "720S": "McLaren",
         "Corvette Stingray": "Chevrolet",
         "Aventador SVJ": "Lamborghini",
         "MX-5 Miata": "Mazda",
         "918 Spyder": "Porsche",
         "Enzo": "Ferrari",
         "Ioniq Hybrid": "Hyundai",
         "LaFerrari": "Ferrari"}

speeds = {"Countach LP500 S 1990": 182,
          "Ioniq Hybrid 2014": 110,
          "Corvette Stingray 2020": 194,
          "Senna 2019": 211,
          "Agera RS 2017": 278,
          "Ultimate Aero 2007": 256,
          "MX-5 Miata 2017": 141,
          "ES 2021": 131,
          "Venom GT 2014": 270,
          "ES 2022": 135,
          "Veyron EB 16.4 2018": 256,
          "Ioniq Hybrid 2016": 115,
          "918 Spyder 2014": 211}

purchase_prices = [24645, 1200000, 28315, 1560000, 845000, 78100, 60900]
mileages = [31244, 50123, 102945, 24642, 30012, 89450, 120324]
years = [2014, 2014, 2017, 2019, 2014, 2021, 2020]

cars_i_bought = ["Ioniq Hybrid", "Venom GT",
                 "MX-5 Miata", "Senna", "918 Spyder", "ES", "Corvette Stingray"]

andrews_cars = []

for item in range(len(cars_i_bought)):
    ####Makes#####
    for makes_model,makes_brand in makes.items():
        if cars_i_bought[item] == makes_model:
            car_marks = makes_brand

    ####speeds#####
    for speeds_key,speeds_value in speeds.items():
        if speeds_key == str(cars_i_bought[item]) + ' ' + str(years[item]):
            car_speeds = speeds_value
            
    car_check = Car(car_marks, cars_i_bought[item], years[item], car_speeds, purchase_prices[item], mileages[item])
    andrews_cars.append(car_check)

    andrews_cars[item].print_info()
   