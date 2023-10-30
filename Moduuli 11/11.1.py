class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f" Julkaisun nimi: {self.nimi} ")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Päätoimittaja on {self.päätoimittaja}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kirjailija: {self.kirjailija}, sivumäärä: {self.sivumaara}")

Lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
Kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

Lehti1.tulosta_tiedot()
Kirja1.tulosta_tiedot()


