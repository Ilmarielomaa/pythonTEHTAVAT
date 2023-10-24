class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0




uusi_auto = auto("ABC-123", 142)

uusi_auto.kiihdytä(30)
uusi_auto.kiihdytä(70)
uusi_auto.kiihdytä(50)


print(f"Auton nopeus: {uusi_auto.tämänhetkinen_nopeus} km/h")

uusi_auto.kiihdytä(-200)

print(f"Auton teki hätäjarrutuksen, nykyinen nopeus: {uusi_auto.tämänhetkinen_nopeus} km/h")
