from ctypes import pythonapi

numero = 1
print("Luvut väliltä 1-1000, jotka on jaollisia kolmella: ")
while numero <= 1000:
    if numero % 3 == 0:
        print(numero)
    numero += 1

while True:
    try:
        tuuma = float(input("Tuuman määrä: "))
        if tuuma < 0:
            print("Suljetaan ohjelma")
            break
        else:
            senttit = tuuma * 2.54
            print(f"{tuuma} tuuma on {senttit} sentteinä")
    except ValueError:
        print("Vain numeroita!")

nmrs = []

while True:
    kayttaja = input("Anna luku: ")
    if kayttaja == "":
        break
    try:
        nmr = float(kayttaja)
        nmrs.append(nmr)
    except ValueError:
        print("Vain numeroita!")

if nmrs:
    pienin = min(nmrs)
    isoin = max(nmrs)
    print(f"pienin numero oli: {pienin}")
    print(f"isoin numero oli: {isoin}")
else:
    print("Lukuja ei annettu")

import random
s_luku = random.randint(1, 10)
arvaus = 0
arvauskerrat = 0

print("Koodi arpoi sinulle salaisen luku aika arvata se.")

while arvaus != s_luku:
    try:
        arvaus_1 = input("Arvaa luku 1-10: ")
        arvaus = int(arvaus_1)
        arvauskerrat += 1
        if arvaus < 1 or arvaus > 10:
            print("Luku ei ole 1-10")
        elif arvaus < s_luku:
            print("Liian pieni arvaus.")
        elif arvaus > s_luku:
            print("Liian suuri arvaus.")
        else:
            print(f"Oikein. luku on {s_luku}! arvasit sen {arvauskerrat} yrityksessä!")
            break
    except ValueError:
        print("Luku ei ole numeraallinen vastaus!")
print("Arvaa luku on nyt ohi kiitos kun pelasit!")



while True:

    kayttaja_tunnus = "python"
    oikea_salasana = "rules"

    try:

       inp_tunnus = input("Käyttäjätunnus: ")
       inp_salasana = input("Anna salasana: ")
    except ValueError:
        print("Invalid input")
    if inp_tunnus == kayttaja_tunnus and inp_salasana == oikea_salasana:
            print("Tervetuloa!")
            break
    else:
            print("Väärä tunnus tai salasana yritä uudelleen!")
