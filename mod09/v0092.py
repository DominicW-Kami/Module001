#toinen tehtävä
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
        print(f"Speed is now {self.speed}")

auto = Auto("", 0, 0, 0)
auto.registery = input("Registery: ")
auto.topspeed = input("Topspeed: ")

while True:
    command = input("Input accelerate or decelerate (or 'quit'): ").lower()
    if command == "accelerate":
        try:
            add = int(input("Accelerate how much?: "))
            auto.accelerate(add)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif command == "decelerate":
        try:
            de_add = int(input("Decelerate how much?: "))
            auto.decelerate(de_add)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif command == "quit":
        break
    else:
        print("Invalid command. Please enter 'accelerate', 'decelerate', or 'quit'.")

print(
    f"The new car's registery is {auto.registery} and the topspeed is "
    f"{auto.topspeed}km/h. The current speed is "
    f"{auto.speed}km/h and the travel distance is {auto.trav}km"
)
