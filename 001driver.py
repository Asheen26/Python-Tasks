class Ride:
    def __init__(self, pickup_location, drop_location, distance):
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.distance = distance
        self.fare = 0

    def calculate_fare(self):
        self.fare = self.distance * 10 

class Driver:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

def assign_driver_to_ride(driver, ride):
    ride.calculate_fare()
    return f"Driver {driver.name} assigned. Estimated fare: {ride.fare}"


ride = Ride("Location A", "Location B", 15)
driver = Driver("John")
passenger = Passenger("Alice")

result = assign_driver_to_ride(driver, ride)
print(result)
