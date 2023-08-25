import random

arpakuutiolista = []
i = 0
summa = 0

arpakuutio = int(input("Syötä arpakuutioiden määrä: "))

while i < arpakuutio:
    j = random.randint(1,6)
    arpakuutiolista.append(j)
    i += 1

for x in arpakuutiolista:
    print(x)
    summa += x

print("Arpakuutioiden lukumäärä on: " + str(summa))



