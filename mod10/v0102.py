class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor  # Elevator always starts at the lowest floor

    def move_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Error: Target floor is outside the elevator's range.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Elevator is already on the highest floor.")

    def floor_down(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Elevator is already on the lowest floor.")

class House:
    def __init__(self, lowest_floor, highest_floor, number_of_elevators):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = []
        for _ in range(number_of_elevators):
            self.elevators.append(Elevator(lowest_floor, highest_floor))

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            print(f"Elevator {elevator_number + 1} is going to floor {target_floor}...")
            elevator.move_to_floor(target_floor)
        else:
            print("Error: Invalid elevator number.")

if __name__ == "__main__":
    house = House(lowest_floor=1, highest_floor=10, number_of_elevators=3)

    print("Elevators in the house:")
    for i, elevator in enumerate(house.elevators):
        print(f"Elevator {i + 1}: Lowest floor {elevator.lowest_floor}, Highest floor {elevator.highest_floor}")

    house.run_elevator(0, 5)
    house.run_elevator(1, 2)
    house.run_elevator(2, 8)
    house.run_elevator(0, 1)
