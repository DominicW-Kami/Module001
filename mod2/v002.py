aa = input('Anna Nimesi: ')
print("Tervehdys, " + aa,"!")
import math

def laske_ympyran_pinta_ala():

    try:

        sade_str = input("Mikä on ympyrän säde? ")
        sade = float(sade_str)


        if sade < 0:
            print("Säde ei voi olla negatiivinen.")
        else:

            pinta_ala = math.pi * (sade ** 2)


            print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")

    except ValueError:

        print("Virheellinen syöte. Ole hyvä ja syötä numero.")


laske_ympyran_pinta_ala()

def laske_suorakulmio():

    try:

        kanta_1 = input ("Mikä on suorakulmion kanta: ")
        kanta_2 =float(kanta_1)

        korkeus_1 = input("Mikä on suorakulmion korkeus: ")
        korkeus_2 = float(korkeus_1)


        if kanta_2 < 0 or korkeus_2 < 0:
            print("Luku ei voi olla negatiivinen.")
        else:

            piiri = 3 * (kanta_2 + korkeus_2)
            pinta_ala = kanta_2 * korkeus_2
            print(f"\nSuorakulmion mitat ovat:")
            print(f"Kanta: {kanta_2:.2f}")
            print(f"Korkeus: {korkeus_2:.2f}")
            print(f"Piiri: {piiri:.2f}")
            print(f"Pinta-ala: {pinta_ala:.2f}")

    except ValueError:

        print("Virheellinen syöte.")

laske_suorakulmio()

def laske_luku():

    try:
        luku_1 = input("Syötä eka luku: ")
        luku1 = int(luku_1)

        luku_2 = input("Syötä toka luku: ")
        luku2 = int(luku_2)

        luku_3 = input("Syötä kolmas luku")
        luku3 = int(luku_3)

        summa = luku1 + luku2 + luku3

        tulo = luku1 * luku2 * luku3

        keskiarvo = summa / 3

        print("\nTulokset:")
        print(f"Syötetyt luvut: {luku1}, {luku2}, {luku3}")
        print(f"Lukujen summa: {summa}")
        print(f"Lukujen tulo: {tulo}")
        print(f"Lukujen keskiarvo: {keskiarvo:.2f}")

    except ValueError:
        print("Virheellinen syöte")
laske_luku()

def muunna_keskiaika_paino():

    try:
        luoti_g = 13.3
        naula_l = 32
        leiviska_n = 20
        naula_g = naula_l * luoti_g
        leiviska_g = leiviska_n * naula_g

        leiviska_1 = input("Syötä leiviköiden määrä: ")
        leiviskat1 = float(leiviska_1)

        naulat_1 = input ("Syötä naulojen määrä: ")
        naulat1 = float(naulat_1)

        luodit_1 = input ("Syötä luotien määrä: ")
        luodit1 = float(luodit_1)

        if leiviskat1 < 0 or naulat1 < 0 or luodit1 <0:
            print("Lukujen pitää olla positiivisia1")
            return

        koko_g = (leiviskat1 * leiviska_g +
                  naulat1 * naula_g +
                  luodit1 * luoti_g)

        koko_kg = int(koko_g / 1000)
        yli_g = koko_g % 1000

        print("\n Muunnostulokset")
        print(f"Syötetty määrä:")
        print(f"  {leiviskat1:.2f} leiviskää")
        print(f"  {naulat1:.2f} naulaa")
        print(f"  {luodit1:.2f} luotia")
        print("\nVastaa kilogrammoina ja grammoina")
        print(f"  {koko_kg} kg ja {yli_g:.2f} g")

    except ValueError:
        print("Virheellinen syöte")
muunna_keskiaika_paino()

import random

def kolminumero_koodi():
    koodi = ""
    for _ in range(3):
        numero = random.randint(0, 9)
        koodi += str(numero)
    return koodi

arvottu_koodi = kolminumero_koodi()
print(f"Arvottu kolmenumeroine koodi on: {arvottu_koodi}")

def nelinumero_koodi():
    koodi1 = ""
    for _ in range(4):
        numero1 = random.randint(1, 6)
        koodi1 += str(numero1)
    return koodi1

arvottu_koodi4 = nelinumero_koodi()
print(f"Arvottu nelinumeroine koodi on: {arvottu_koodi4}")