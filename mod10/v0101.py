class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def move_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print(f"Error: Target floor {target_floor} is outside the elevator's range ({self.lowest_floor}-{self.highest_floor}).")
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


if __name__ == "__main__":
    my_elevator = Elevator(lowest_floor=1, highest_floor=10)

    print(f"Elevator starts on floor {my_elevator.current_floor}")
    print("\nMoving to floor 5...")
    my_elevator.move_to_floor(5)
    print("\nMoving back to floor 1...")
    my_elevator.move_to_floor(1)
