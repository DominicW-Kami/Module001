#ensimmäinen tehtävä
class Auto:
    def __init__(self, registery, topspeed, speed, trav):
        self.registery = registery
        self.topspeed = topspeed
        self.speed = speed
        self.trav = trav
auto = Auto(" ", 0, 0, 0)
Auto.registery = input("Rekisteri: ")
Auto.topspeed = input("Huippunopeus: ")
Auto.speed = 0
Auto.trav = 0
print(f"Uuden auton rekisteri on {Auto.registery} ja huippunopeus {Auto.topspeed}km/h auton hetkellinen nopeus on {Auto.speed}km/h ja kuljettumatka {Auto.trav}km")
#toinen tehtävä
