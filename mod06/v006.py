import random
def noppakuusi (tahkotlkm):
    return random.randint(1, tahkotlkm)
def heittaminen ():
    nmrnoppa = input("Anna nopan tahkojen määrä: ")
    tahkotlkm = int(nmrnoppa)
    heittoja = 0
    while True:
        silmaluku = noppakuusi(tahkotlkm)
        heittoja += 1
        print(f"Heitto {heittoja}: {silmaluku}")
        if silmaluku == tahkotlkm:
            print(f"{tahkotlkm} tuli. Heittäminen nyt loppuu.")
            break
heittaminen()

def gallons(gallonat):
    litrat = gallonat * 3.785
    return litrat
def muuttumis():
    while True:
        try:
            gallonat = float(input("Anna bensiinin määrä galloneissa: "))
            if gallonat < 0:
                print("Lopetetaan muunnokset")
                break
            litrat = gallons(gallonat)
            print(f"{gallonat:.2f} gallonaa on {litrat:.2f} litroissa")
        except ValueError:
            print("Virheellinen syöte")
if __name__ == "__main__":
    muuttumis()

def parametrilist(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa
def lista():
    testilista = [1, 2, 3, 4, 5]
    summa = parametrilist(testilista)
    print(f"Lista 1 {testilista} summa on: {summa}")
if __name__ == "__main__":
    lista()

def parittomat(lk):
    parilliset = [lu for lu in lk if lu % 2 == 0]
    return parilliset
def testi():
    testilist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    uusi_lista = parittomat(testilist)
    print(f"Alkuperäinen {testilist}")
    print(f"Parilliset {uusi_lista}")
if __name__ == "__main__":
    testi()
import math
def pizza_per_neliometri(diametri_cm, hinta_euro):
    radius1 = diametri_cm / 2 / 100
    area_nm = math.pi * radius1**2
    hinta_neliometri = hinta_euro / area_nm
    return hinta_neliometri
def paaohjelma():
    pizza1d = float(input("Anna pizza 1 leveys (cm): "))
    pizza1h = float(input("Anna pizza 1 hinta (eur): "))
    pizza2d = float(input("Anna pizza 2 leveys (cm): "))
    pizza2h = float(input("Anna pizza 2 hinta (eur): "))
    hinta_n1 = pizza_per_neliometri(pizza1d, pizza1h)
    hinta_n2 = pizza_per_neliometri(pizza2d, pizza2h)
    print(f"Pizza 1 hinta per neliömetri: {hinta_n1:.2f}")
    print(f"Pizza 2 hinta per neliömetri: {hinta_n2:.2f}")
    if hinta_n1 < hinta_n2:
        print("Pizza 1 on parempi hinta suhteelta")
    elif hinta_n2 < hinta_n1:
        print("Pizza 2 on parempi hinta suhteelta")
    else:
        print("Molemilla on sama hinta")
if __name__ == "__main__":
    paaohjelma()
