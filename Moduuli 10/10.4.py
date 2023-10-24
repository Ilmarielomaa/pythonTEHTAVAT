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

class Kilpailu:
    tunti = 0

    def __init__(self, kilpailun_nimi, kilpailun_pituus):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistuvat_autot = self.auto_luonti()

    def auto_luonti(self):
        autolista = []
        for i in range(1, 11):
            auto = Auto(f"ABC-{i}", random.randint(100, 200))
            autolista.append(auto)
        return autolista

    def tunti_kuluu(self):
        Kilpailu.tunti += 1
        for auto in self.osallistuvat_autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
        if Kilpailu.tunti == 10:
            Kilpailu.tunti = 0
            self.tulosta_tilanne()

    def tulosta_tilanne(self):
        print("\nKilpailun tilanne:\n")
        for auto in self.osallistuvat_autot:
            print(f"Auto {auto.rekisteritunnus} nopeus: {auto.tamanhetkinen_nopeus} km/h"
                  f" kuljettu matka: {auto.kuljettu_matka} kilometriä.")

    def kilpailu_ohi(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettu_matka >= self.kilpailun_pituus:
                return True
        return False

kilpailu = Kilpailu("Suuri romuralli", 8000)
gamerunning = not kilpailu.kilpailu_ohi()

while gamerunning:
    kilpailu.tunti_kuluu()
    gamerunning = not kilpailu.kilpailu_ohi()

kilpailu.tulosta_tilanne()

for auto in kilpailu.osallistuvat_autot:
    if auto.kuljettu_matka >= kilpailu.kilpailun_pituus:
        print(f"Voittaja: {auto.rekisteritunnus}")
