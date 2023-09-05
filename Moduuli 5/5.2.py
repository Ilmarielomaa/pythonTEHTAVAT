numerot = []

while True:
    syote = input("syötä luku, tyhjä merkkijono lopettaa: ")

    if syote == "":
        break

    try:
        luku = float(syote)
        numerot.append(luku)
    except ValueError:
        print("Virheellinen luku, syötä kelvollinen luku: ")

if len(numerot) < 5:
    print("Liian vähän lukuja, tarvitaan väh. 5 lukua. ")
else:
    numerot.sort(reverse=True)
    print("Viisi lukua suurimmasta pienimpään: ")
    for luku in numerot[:5]:
        print(luku)

