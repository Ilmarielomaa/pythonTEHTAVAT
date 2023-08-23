laskuri = 0
while laskuri < 5:
    laskuri += 1
    kayttajatunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    if kayttajatunnus == "python" and salasana == "rules":
        print("TERVETULOA.")

    if laskuri == 5:
        print("PÄÄSY EVÄTTY!")





