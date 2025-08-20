import math
import random

def kuhan_mitta():

    try:
        pituus_1 = random.randint(20,80)
        pituus1 = float(pituus_1)
        print(f"\nKalastaja: Kuhan pituus on: {pituus_1}")

        alamitta = 37.0

        if pituus1 < alamitta:
            ps = alamitta - pituus1
            print(f"\nKuha on alamittainen. Laske se takaisin!")
            print(f"Puuttivia senttimetrejä alimasta sallitusta pyyntimitasta: {ps:.1f} cm")
        else:
            print(f"\nHieno saalis! Kuha on riittävän suuri pyydyttäväksi!")
            print(f"Pituus: {pituus1:.1f} cm")
    except ValueError:
        print("Virheellinen syöte.")
kuhan_mitta()