import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeudenmuutos):
        if (self.nopeus + nopeudenmuutos > self.huippunopeus):
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeudenmuutos

    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nopeus * tuntimäärä

class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self. akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self. bensatankki = bensatankki


Sähköauto = Sähköauto("ABC-15", 180, 52.5)
Polttomoottoriauto = Polttomoottoriauto("ABC-123", 165, 32.2)


Sähköauto.nopeus = 100
Polttomoottoriauto.nopeus = 30
Sähköauto.kulje(3)
Polttomoottoriauto.kulje(3)

print(f"Sähköauton {Sähköauto.rekisteritunnus} kuljettu matka: {Sähköauto.kuljettumatka} km")
print(f"Polttomoottoriauton {Polttomoottoriauto.rekisteritunnus} kuljettu matka: {Polttomoottoriauto.kuljettumatka} km" )
