#neljäs tehtävä
import random
class Auto:
    def __init__(self, registery, topspeed, speed, trav):
        self.registery = registery
        self.topspeed = int(topspeed)
        self.speed = int(speed)
        self.trav = int(trav)

    def accelerate(self):
        change = random.randint(-10, 15)
        self.speed += change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.topspeed:
            self.speed = self.topspeed

    def kulje(self, tunnit):
        matka_tunnissa = self.speed * tunnit
        self.trav += matka_tunnissa

autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus, 0, 0))
tunti = 0
while True:
    tunti += 1
    for auto in autot:
        auto.accelerate()
        auto.kulje(1)

    voittaja = None
    for auto in autot:
        if auto.trav >= 10000:
            voittaja = auto
            break

    if voittaja:
        print(f"Kilpailu päättyi {tunti} tunnin jälkeen!")
        break

print("\n--- Kilpailun tulokset ---")
print("-" * 40)
print(f"{'Rekisteri':<10} {'Huippunopeus':<15} {'Nopeus':<8} {'Matka':<10}")
print("-" * 40)
for auto in autot:
    print(f"{auto.registery:<10} {auto.topspeed:<15} {auto.speed:<8} {auto.trav:<10.2f}")
print("-" * 40)