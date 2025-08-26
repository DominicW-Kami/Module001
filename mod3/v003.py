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
hyttiluokka = input("Syötä hytinluokka (LUX, A, B, C,): ")
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella. ")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print ("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

Sukupuoli = input("Syötä biologinen sukupuolesi (mies/nainen): ")
while True:
    try:
        hemoglobiini = float(input("Syötä hemoglobiiniarvosi (g/l): "))
        break
    except ValueError:
        print("Virheellinen syöte")
if Sukupuoli == "mies":
    if 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on korkea.")
elif Sukupuoli == "nainen":
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen syöte")

vuosi = int(input("Syötä vuosiluku: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0 ):
    print(f"{vuosi} on karkausvuosi. ")
else:
    print(f"{vuosi} ei ole karkausvuosi.")
