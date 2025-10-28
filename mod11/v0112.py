class Auto:
    def __init__(self, registery, topspeed, speed, trav):
        self.registery = str(registery)
        self.topspeed = int(topspeed)
        self.speed = int(speed)
        self.trav = int(trav)

    def accelerate(self, increase):
        self.speed += increase
        if self.speed > self.topspeed:
            self.speed = self.topspeed
        print(f"Speed is now {self.speed} km/h")

    def decelerate(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        if self.speed > self.topspeed:
            self.speed = self.topspeed
        print(f"Speed is now {self.speed} km/h")

    def move(self, hours):
        metersmoved = self.speed * hours
        self.trav += metersmoved
        print(f"The car has traveled now {self.trav} km")

class ElectricCar(Auto):
    def __init__(self, registery, topspeed, battery_capacity):
        super().__init__(registery, topspeed, 0, 0)
        self.battery_capacity = battery_capacity

    def print_info(self):
        print(f"Electric Car - Registery: {self.registery}, Topspeed: {self.topspeed} km/h, Battery Capacity: {self.battery_capacity} kWh, Odometer: {self.trav} km")

class GasolineCar(Auto):
    def __init__(self, registery, topspeed, fuel_tank_size):
        super().__init__(registery, topspeed, 0, 0)
        self.fuel_tank_size = fuel_tank_size

    def print_info(self):
        print(f"Gasoline Car - Registery: {self.registery}, Topspeed: {self.topspeed} km/h, Fuel Tank Size: {self.fuel_tank_size} liters, Odometer: {self.trav} km")

if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(100)
    electric_car.move(3)

    gasoline_car.accelerate(120)
    gasoline_car.move(3)

    print("\n--- Car Odometer Readings ---")
    electric_car.print_info()
    gasoline_car.print_info()