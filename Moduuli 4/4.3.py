num = str(0)
pienin = int(0)
suurin = int(0)
syöte = "0"

while syöte != "":
    syöte = (input("syötä luku: "))
    if syöte != "":
        num = int(syöte)
        if num > suurin:
            suurin = num
        elif num < pienin:
            pienin = num

print("suurin numero: " + str(suurin) + " ja" + " pienin numero: " + str(pienin))

