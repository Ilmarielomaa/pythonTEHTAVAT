import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus
    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit

autot = []

for i in range(1,11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)
    print(f"Auton rekisteritunnus: {auto.rekisteritunnus}"
          f" ja huippunopeus: {auto.huippunopeus} km/h. ")

print("\nKilpailu alkaa!")

gamerunning = True

while gamerunning:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            gamerunning = False
        else:
            None

    for auto in autot:
        print(f"Auton {auto.rekisteritunnus} nopeus on {auto.tamanhetkinen_nopeus} km/h."
              f" Auton {auto.rekisteritunnus} kuljettu matka on nyt {auto.kuljettu_matka} kilometriä.")



