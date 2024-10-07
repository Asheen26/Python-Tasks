class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def details(self):
        print(f"Car Details: {self.brand} {self.model}, Year: {self.year}")

class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def details(self):
        print(f"Bike Details: {self.brand} {self.model}, Year: {self.year}")

def show_details(vehicle):
    vehicle.details()

my_car = Car("BMW","M5",2024)
my_bike=Bike("yamaha","r1",2000)
show_details(my_car)
show_details(my_bike)


