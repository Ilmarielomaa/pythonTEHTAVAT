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
    def kulje(self, aika):
        uusi_matka = aika * 60
        self.kuljettu_matka = self.kuljettu_matka + uusi_matka



uusi_auto = auto("ABC-123", 142)

uusi_auto.kulje(1.5)

print(f"Auton kulki {1.5}h vauhdilla 60 km/h. Nykyinen kuiljettu matka {uusi_auto.kuljettu_matka} km.")

