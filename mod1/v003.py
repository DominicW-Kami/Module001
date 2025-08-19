import math
def laske():

    try:
        sade1 = input('Mikä on ympyrän säde? ')
        sade2 = float(sade1)
        if sade2 < 0:
            print("Säde ei voi olla negatiivinen luku!")
        else:
           pinta_ala = math.pi * (sade2 ** 2)
           print(f"Ympyrän pinta-ala on: {pinta_ala:.2f} kun säde on {sade2:.2f}")
    except ValueError:
           print("Virheellinen syöte.")


