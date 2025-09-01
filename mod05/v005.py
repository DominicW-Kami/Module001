import random
def arpakuutio_luvut ():
    try:
        syote = input("Syötä arpakuution määrä: ")
        syote1 = int(syote)
        if syote1 <= 0:
            print("Syötä positiivinen luku")
            return
        silmalukujen_summa = 0
        heitetyt_silmaluvut = []
        for _ in range(syote1):
            silmaluku = random.randint(1,6)
            heitetyt_silmaluvut.append(silmaluku)
            silmalukujen_summa += silmaluku
        print(f"Heitetyt silmäluvut: {heitetyt_silmaluvut}")
        print(f"Silmälukujen summa on: {silmalukujen_summa}")
    except ValueError:
        print("Virheellinen syöte")
arpakuutio_luvut()

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
    nmrs.sort(reverse=True)
    top5 = nmrs[:5]
    print("\nViisi isointa numeroa ovat: ")
    for num in top5:
        print(num)
else:
    print("No numbers were entered.")

def alkuluku_25 (luku):
    if luku <= 1:
        return False
    for i in range(2, int(luku**0.5) +1):
        if luku % i == 0:
            return False
    return True
try:
    numb = input("Anna kokonaisluku: ")
    numero = int(numb)
    if alkuluku_25(numero):
        print(f"Luku {numero} on alkuluku.")
    else:
        print(f"Luku {numero} ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte")

kaupunki_lista = []
print("Syötä kaupunkien nimet: ")
for i in range(5):
    kaupunki = input(f"Kaupunki {i+1}: ")
    kaupunki_lista.append(kaupunki)
print("\nKaupunkien nimet ovat: ")
for kaupunki in kaupunki_lista:
    print(kaupunki)