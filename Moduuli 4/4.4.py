import random

luku = int(random.randint(1, 10))
arvaus = int(0)

while arvaus != luku:
    arvaus = int(input("arvaa luku: "))
    if arvaus < luku:
        print("liian pieni arvaus")
    elif arvaus > luku:
        print("liian suuri arvaus")

print("oikein")