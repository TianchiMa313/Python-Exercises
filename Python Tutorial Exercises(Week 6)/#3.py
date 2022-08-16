'''
Create a new class CarCollection to help Andrew manage all his cars. 

count() method:
'return len(andrews_cars)' returns the number of items in andrews_cars.

total_value() method:
Use a for loop and a variable called 'new_value' to track the total amount.
'num.estimate_value()' = the estimate vlaue for each car then use '+=' add the estimate vlaue to 'new_value'. 
Return 'new_value' to get the total estimate value at the end.

print_fastest_car() method:
To get the car speeds:
Use a for loop to get the max speed value for each car and append them into a new list called max_speed_list.
To get the car marks:
Use the same technique to get the car makes and append them into a new list called marks_list.
Find the largest number in the list.
Set the first element as the largest number candidate. Loop through the list of numbers. 
Update the largest number candidate if a number is greater than it.
print the fastest car's info at the end.

print_cheapest_car() method:
Use the same technique as print_fastest_car() method. But this time we look for the smallest number in the list.
print the cheapest car's info at the end.
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
            # print(car_speeds)
            
    car_check = Car(car_marks, cars_i_bought[item], years[item], car_speeds, purchase_prices[item], mileages[item])
    
    andrews_cars.append(car_check)
    # andrews_cars[item].print_info()
    # print(car_check.max_speed)

class CarCollection(Car):
    
    def __init__(self, car):
        self.car = car

    def count(self):
        return len(andrews_cars)

    def total_value(self):
        new_value = 0
        for num in andrews_cars:
            new_value += num.estimate_value()
        return new_value

    def print_fastest_car(self):
        max_speed_list = []
        for sp in andrews_cars:
            max_speed_list.append(sp.max_speed)

        marks_list = []
        for mk in andrews_cars:
            marks_list.append(mk.make)

        max = max_speed_list[0]
        a = 0
        for x in max_speed_list:
            if x > max:
                max = x
                a += 1
        print(f'The fastest car from this collection is the {years[a]} {marks_list[a]} {cars_i_bought[a]}')
        return andrews_cars[a].print_info()

    def print_cheapest_car(self):
        marks_list2 = []
        for mk in andrews_cars:
            marks_list2.append(mk.make)

        z = []
        for num in andrews_cars:
            z.append(num.estimate_value())
            min = z[0]
            b = 0
            for x in z:
                if x < min:
                    min = x
                    b += 2

        print(f'The cheapest car from this collection is the {years[b]} {marks_list2[b]} {cars_i_bought[b]}, it is currently estimated to be ${min}.')
        return andrews_cars[b].print_info()

andrews_car_collection = CarCollection(andrews_cars)
print(andrews_car_collection.count()) 
print(andrews_car_collection.total_value())     
andrews_car_collection.print_fastest_car()
andrews_car_collection.print_cheapest_car()