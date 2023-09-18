class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def tulosta_ominaisuudet(self):
        print("Auton tiedot:")
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus: {self.huippunopeus} km/h")
        print(f"tämänhetkinen_nopeus: {self.tämänhetkinen_nopeus} km/h")
        print(f"kuljettu_matka: {self.kuljettu_matka} km")

uusi_auto = auto("ABC-123", 142)
uusi_auto.tulosta_ominaisuudet()


