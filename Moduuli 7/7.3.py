import json

lentoasemat = []

def syota_lentoasema():
    icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")

    for lentoasema in lentoasemat:
        if lentoasema["icao"] == icao_koodi:
            print("ICAO-koodi on jo käytössä.")
            return

    nimi = input("Syötä lentoaseman nimi: ")

    lentoasema = {"icao": icao_koodi, "nimi": nimi}
    lentoasemat.append(lentoasema)

def hae_lentoasema():
    icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")

    for lentoasema in lentoasemat:
        if lentoasema["icao"] == icao_koodi:
            print(lentoasema["nimi"])
            return

    print("Lentokenttää ei löytynyt.")
def lopeta():
    print("Lopetan.")
    exit()

while True:
    print("Valitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        syota_lentoasema()
    elif valinta == "2":
        hae_lentoasema()
    elif valinta == "3":
        lopeta()
    else:
        print("Virheellinen valinta.")
