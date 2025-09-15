def vuodenajat():
    vuodenaiai = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi",)
    while True:
        try:
            kuukausi = int(input("Anna kuukauden numero (1-12): "))
            if 1<= kuukausi <= 12:
                 vuodenaika = vuodenaiai[kuukausi - 1]
                 print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}")
                 break
            else:
                print("anna luku 1-12")
        except ValueError:
            print("Virheellinen input")
vuodenajat()

import random

def hallinoi():
    syötetyt_nimet = set()
    nimet_listana = []
    print("Syötä nimiä, Lopeta painamalla enter")
    while True:
        nimi = input("Syötä nimi: ").strip()
        if not nimi:
            break
        if nimi in syötetyt_nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            syötetyt_nimet.add(nimi)
            nimet_listana.append(nimi)
    print("\n--- Syötetyt nimet ---")
    random.shuffle(nimet_listana)
    for yksittäinen_nimi in nimet_listana:
        print(yksittäinen_nimi)
hallinoi()

def lentoasemia():
    lentoasemat = {}
    while True:
        print("\nValitse toiminto:")
        print("1 Syötä uusi lentoasema")
        print("2 Hae lentoaseman tiedot")
        print("3 Lopeta")
        valinta = input("Syötä valintasi (1-3): ")
        if valinta == "1":
            icao_koodi = input("Syötä lentoaseman ICAO-koodi").upper()
            nimi = input("Syötä lentoaseman nimi: ")
            lentoasemat[icao_koodi] = nimi
            print(f"Lentoasema '{nimi}' ({icao_koodi}) lisätty")
        elif valinta == "2":
            icao_koodi_haku = input("Syötä haettavan lentoaseman ICAO-koodi").upper()
            if icao_koodi_haku in lentoasemat:
                nimi_haku = lentoasemat[icao_koodi_haku]
                print(f"ICAO-koodia {icao_koodi_haku} vastaava lentoasema on : {nimi_haku}")
            else:
                print(f"Virhe: ICAO-koodilla {icao_koodi_haku} ei löytynyt lentoasemaa")
        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta.")
lentoasemia()