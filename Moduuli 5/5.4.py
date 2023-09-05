kaupungit = []

kaupunki = input("Anna ensimmäinen kaupunki tai lopeta painamalla Enter: ")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki tai lopeta painamalla Enter: ")

for kaupunki in kaupungit:
    print (f"{kaupunki}")
