num = str(0)
pienin = int(0)
suurin = int(0)
syote = "0"

while syote != "":
    syote = (input("syötä luku: "))
    if syote != "":
        num = int(syote)
        if num > suurin:
            suurin = num
        elif num < pienin:
            pienin = num

print("suurin numero: " + str(suurin) + " ja" + " pienin numero: " + str(pienin))