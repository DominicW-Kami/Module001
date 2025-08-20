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