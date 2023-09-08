import random

nimijoukko = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break

    if nimi not in nimijoukko:
        print("Uusi nimi", nimi)
        nimijoukko.add(nimi)
    else:
        print("Aiemmin syötetty nimi", nimi)

nimet = list(nimijoukko)
random.shuffle(nimet)
for nimi in nimet:
    print(nimi)