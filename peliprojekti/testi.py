import random
import math


class Esine:
     def __init__(self, nimi, paino,):
        self.nimi = nimi
        self.paino = paino

class Miekka(Esine):
    def __init__(self,nimi,paino,):
        super().__init__(nimi, paino,)
        self.vahinko = random.randint(5-12)

def lyönti():
    if Miekka == False:
        print("Et voi lyödä ilman miekkaa!")
    if Miekka == True:
        vahinko = random.randint(4,12)
        print(f"Lyöntisi teki {vahinko} vahinkoa!")

lyönti()


class Humanoidi:
     def __init__(self,nimi, ikä, sijainti=None,):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.hp = 30

class Pelaaja(Humanoidi):
    def __init__(self,nimi, ikä, sijainti=None,):
        super().__init__(nimi, ikä, sijainti,)
        self.inventaario = []
        self.hp = 50
    def osta_tavara(self, tavara):
            self.inventaario.append(tavara)
            print (f"Reppuun lisättiin: {tavara}")
    def löysit_tavaran(self, tavara):
        self.lisaa_tavara(tavara)
        print (f"Löysit tavaran: {tavara}")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0 

    def kiihdytä(self, kmh):
        uusi_nopeus = self.nopeus + kmh

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


#lyönti()
