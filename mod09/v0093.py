#kolmas tehtävä
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
        print(f"Speed is now {self.speed}")

    def decelerate(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        if self.speed > self.topspeed:
            self.speed = self.topspeed
        print(f"Speed is now {self.speed}")
    def move(self, hours):
        metersmoved = self.speed * hours
        self.trav += metersmoved
        print(f"The car has traveled now {self.trav}")

auto = Auto("", 0, 0, 0)
auto.registery = input("Registery: ")
auto.topspeed = int(input("Topspeed: "))

while True:
    command = input("Input accelerate, decelerate, kulje, or quit: ").lower()
    if command == "accelerate":
        try:
            add = int(input("Accelerate how much (km/h)?: "))
            auto.accelerate(add)
            try:
                hours = float(input("How many hours will you drive at this speed?: "))
                auto.move(hours)
            except ValueError:
                print("Invalid input for hours. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number for speed increase.")
    elif command == "decelerate":
        try:
            de_add = int(input("Decelerate how much (km/h)?: "))
            auto.decelerate(de_add)
            try:
                hours = float(input("How many hours will you drive at this speed?: "))
                auto.move(hours)
            except ValueError:
                print("Invalid input for hours. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number for speed decrease.")
    elif command == "kulje":
        try:
            tunnit = float(input("How many hours to travel?: "))
            auto.move(hours)
        except ValueError:
            print("Invalid input. Please enter a number for hours.")
    elif command == "quit":
        break

print(
    f"\n--- Car Summary ---\n"
    f"Registery: {auto.registery}\n"
    f"Topspeed: {auto.topspeed} km/h\n"
    f"Current Speed: {auto.speed} km/h\n"
    f"Total Travel Distance: {auto.trav} km"
)