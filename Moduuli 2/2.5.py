leiviska = int(7000)
naula = int(400)
luoti = int(10)
summa = int(0)
kilogramma = int(0)
gramma = int(0)

leiviskat = int(input("Anna leiviskat: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna naulata: "))

summa = leiviska * leiviska + naula * naulat + luoti * luodit

kilo = summa / 1000
gramma = summa % 1000
kilo = int(kilo)

print("Massa nykymittojen mukaan: " + str(kilo ) + " Kiloa ja " + str(gramma) + " gramma.")