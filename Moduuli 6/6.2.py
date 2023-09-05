import random
def arpakuutio(tahkot):
    noppa = int(0)

    while noppa < tahkot:
        noppa = int(random.randint(1, tahkot))
        print(noppa)
tahkot = int(input("syötä tahkojen määrä:" ))
arpakuutio(tahkot)

